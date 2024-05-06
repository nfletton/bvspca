import time
from os import path
from os.path import expanduser

from fabric.api import env, put, sudo, task
from fabric.context_managers import prefix
from fabric.contrib.project import rsync_project
from fabric.operations import run

with open(expanduser('~') + '/ansible-playbooks/env/bvspca.py', 'r') as config:
    exec(config.read())


EXCLUDES = [
    '/.*',
    '**/*.pyc',
    '**/__pycache__',
    '**/.sass-cache',
]

GROUP_NO_PERMS = [
    'config',
    'requirements',
    'bvspca',
    'manage.py',
]

GROUP_READ_PERMS = [
    'staticfiles',
    'media',
]

GROUP_RW_PERMS = [
]

DJANGO_SETTINGS_MODULE = 'config.settings.production'

@task
def dry_run():
    deploy_full(dry_run='yes')


@task
def deploy_code():
    deploy_full(venv='no')


@task
def deploy_full(dry_run='no', venv='yes'):
    upload_files(dry_run)
    run('mkdir -p backups')
    run('mkdir -p staticfiles')
    run('mkdir -p logs')
    if dry_run == 'no':
        set_permissions()
        if venv == 'yes':
            rebuild_venv()
        collect_static()
        _stop_gunicorn()
        migrate()
        _start_gunicorn()
        _reload_nginx()


@task
def collect_static():
    with prefix('source ' + ACTIVATE_SCRIPT):
        run(PYTHON_EXECUTABLE + ' manage.py collectstatic --no-input')


@task
def migrate():
    with prefix('source ' + ACTIVATE_SCRIPT):
        run(PYTHON_EXECUTABLE + ' manage.py migrate')


@task
def set_permissions():
    for file in GROUP_NO_PERMS:
        remote_dir = env.remote_dir + '/' + file
        run(
            'find ' + remote_dir + r' -type d -exec chmod 700 {} \; && find ' + remote_dir + r' -type f -exec chmod 600 {} \;')
    for file in GROUP_READ_PERMS:
        remote_dir = env.remote_dir + '/' + file
        run(
            'find ' + remote_dir + r' -type d -exec chmod 750 {} \; && find ' + remote_dir + r' -type f -exec chmod 640 {} \;')
    for file in GROUP_RW_PERMS:
        remote_dir = env.remote_dir + '/' + file
        run(
            'find ' + remote_dir + r' -type d -exec chmod 770 {} \; && find ' + remote_dir + r' -type f -exec chmod 660 {} \;')


@task
def upload_files(dry_run='no', media=False):
    rsync_project(remote_dir=env.remote_dir,
                  local_dir=env.local_dir + '/bvspca',
                  default_opts='-thrvz',
                  delete=True,
                  extra_opts='--dry-run' if dry_run == 'yes' else '',
                  exclude=EXCLUDES)
    if media:
        rsync_project(remote_dir=env.remote_dir,
                      local_dir=env.local_dir + '/media',
                      default_opts='-thrvz',
                      delete=True,
                      extra_opts='--dry-run' if dry_run == 'yes' else '')
    rsync_project(remote_dir=env.remote_dir,
                  local_dir=env.local_dir + '/config',
                  default_opts='-thrvz',
                  delete=True,
                  extra_opts='--dry-run' if dry_run == 'yes' else '')
    rsync_project(remote_dir=env.remote_dir,
                  local_dir=env.local_dir + '/requirements',
                  default_opts='-thrvz',
                  delete=True,
                  extra_opts='--dry-run' if dry_run == 'yes' else '')
    rsync_project(remote_dir=env.remote_dir,
                  local_dir=env.local_dir + '/manage.py',
                  default_opts='-thrvz',
                  delete=True,
                  extra_opts='--dry-run' if dry_run == 'yes' else '')
    rsync_project(remote_dir=env.remote_dir,
                  local_dir=env.local_dir + '/.env.production',
                  default_opts='-thrvz',
                  delete=True,
                  extra_opts='--dry-run' if dry_run == 'yes' else '')


@task
def outdated_packages():
    run(PIP_EXECUTABLE + ' list -o')


@task
def rebuild_venv():
    if run('test -d %s' % VENV_DIR).succeeded:
        run('rm -rf ' + VENV_DIR)
    run('python3 -m venv ' + VENV_DIR)
    run(PIP_EXECUTABLE + ' install --upgrade pip', shell=True)
    run(PIP_EXECUTABLE + ' install -U setuptools', shell=True)
    run(PIP_EXECUTABLE + ' install -r requirements/production.txt', shell=True)
    _set_environment_variable('DJANGO_READ_DOT_ENV_FILE', 'True', ACTIVATE_SCRIPT)
    _set_environment_variable('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE, ACTIVATE_SCRIPT)


def _set_environment_variable(name, value, location):
    command = 'export ' + name + '="' + value + '"'
    run("echo '" + command + "' >> " + location)


@task
def load_live_db(dump_file):
    """
    Load the provided Postgres SQL file into the project db
    """
    run('mkdir ~/tmp', warn_only=True, quiet=True)
    put(dump_file, 'tmp/')
    basename = path.basename(dump_file)
    remote_dump_file = 'tmp/' + basename
    _stop_gunicorn()
    statement = "DROP DATABASE " + DB_NAME + ";"
    _run_psql_statement(statement, warn_only=True)
    statement = "CREATE DATABASE " + DB_NAME + " LC_COLLATE='en_CA.UTF-8' LC_CTYPE='en_CA.UTF-8' TEMPLATE='template0';"
    _run_psql_statement(statement)
    statement = "GRANT ALL ON DATABASE " + DB_NAME + " TO " + PROJECT_USER + ";"
    _run_psql_statement(statement)
    _import_psql_data(remote_dump_file)
    _start_gunicorn()


def _run_psql_statement(statement, **kvargs):
    run('psql -U postgres -d postgres -c "' + statement +'"', **kvargs)


def _import_psql_data(sql_file, **kvargs):
    run('psql -U postgres -d postgres -d ' + DB_NAME + ' -f ' + sql_file, **kvargs)


@task
def backup_db():
    """
    Backup the project database
    """
    backup_name = DB_NAME + time.strftime("-%Y%m%d-%H%M%S.sql")
    run('mkdir ~/backups', warn_only=True, quiet=True)
    run('pg_dump --inserts --create -U postgres ' + DB_NAME + ' > ~/backups/' + backup_name)


@task
def restart_app():
    _stop_gunicorn()
    _start_gunicorn()
    _reload_nginx()


def _stop_gunicorn():
    sudo('sudo supervisorctl stop ' + PROJECT_USER)


def _start_gunicorn():
    sudo('sudo supervisorctl update ' + PROJECT_USER)
    sudo('sudo supervisorctl start ' + PROJECT_USER)


def _reload_nginx():
    sudo('sudo service nginx reload')

if __name__ == '__main__':
    dry_run()
