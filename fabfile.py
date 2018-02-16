import time
from os import path
from os.path import expanduser

from fabric.api import env, put, sudo, task
from fabric.context_managers import prefix
from fabric.contrib.files import sed
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

GROUP_NO_PERMISSIONS = [
    'config',
    'requirements',
    'bvspca',
    'manage.py',
]

GROUP_READ_PERMISSIONS = [
    'staticfiles',
    'media',
]

GROUP_RW_PERMISSIONS = [
]


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
        _stop_gunicorn()
        if venv == 'yes':
            rebuild_venv()
        collect_static()
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
    for file in GROUP_NO_PERMISSIONS:
        remote_dir = env.remote_dir + '/' + file
        run(
            'find ' + remote_dir + ' -type d -exec chmod 700 {} \; && find ' + remote_dir + ' -type f -exec chmod 600 {} \;')
    for file in GROUP_READ_PERMISSIONS:
        remote_dir = env.remote_dir + '/' + file
        run(
            'find ' + remote_dir + ' -type d -exec chmod 750 {} \; && find ' + remote_dir + ' -type f -exec chmod 640 {} \;')
    for file in GROUP_RW_PERMISSIONS:
        remote_dir = env.remote_dir + '/' + file
        run(
            'find ' + remote_dir + ' -type d -exec chmod 770 {} \; && find ' + remote_dir + ' -type f -exec chmod 660 {} \;')


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


@task
def outdated_packages():
    run(PIP_EXECUTABLE + ' list -o')


@task
def rebuild_venv():
    if run('test -d %s' % VENV_DIR).succeeded:
        run('rm -rf ' + VENV_DIR)
    run('python3 -m venv ' + VENV_DIR)
    run(PIP_EXECUTABLE + ' install -r requirements/production.txt', shell=True)
    run(PIP_EXECUTABLE + ' install -U pip', shell=True)
    run(PIP_EXECUTABLE + ' install -U setuptools', shell=True)
    _set_environment_variable('DJANGO_SECRET_KEY', DJANGO_SECRET_KEY, ACTIVATE_SCRIPT)
    _set_environment_variable('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE, ACTIVATE_SCRIPT)
    _set_environment_variable('DJANGO_ADMIN_URL', DJANGO_ADMIN_URL, ACTIVATE_SCRIPT)
    _set_environment_variable('WAGTAIL_ADMIN_URL', WAGTAIL_ADMIN_URL, ACTIVATE_SCRIPT)
    _set_environment_variable('DATABASE_URL', DATABASE_URL, ACTIVATE_SCRIPT)
    _set_environment_variable('PATH', PATH, ACTIVATE_SCRIPT)
    _set_environment_variable('ADDTHIS_PUB_ID', ADDTHIS_PUB_ID, ACTIVATE_SCRIPT)
    _set_environment_variable('RECAPTCHA_SITE_KEY', RECAPTCHA_SITE_KEY, ACTIVATE_SCRIPT)
    _set_environment_variable('RECAPTCHA_SECRET_KEY', RECAPTCHA_SECRET_KEY, ACTIVATE_SCRIPT)
    _set_environment_variable('GOOGLE_ANALYTICS_ID', GOOGLE_ANALYTICS_ID, ACTIVATE_SCRIPT)
    _set_environment_variable('MAILCHIMP_USERNAME', MAILCHIMP_USERNAME, ACTIVATE_SCRIPT)
    _set_environment_variable('MAILCHIMP_SECRET_KEY', MAILCHIMP_SECRET_KEY, ACTIVATE_SCRIPT)
    _set_environment_variable('MAILCHIMP_LIST_ID', MAILCHIMP_LIST_ID, ACTIVATE_SCRIPT)
    _set_environment_variable('MAILCHIMP_TEMPLATE_ID', MAILCHIMP_TEMPLATE_ID, ACTIVATE_SCRIPT)
    _set_environment_variable('MAILCHIMP_SUBJECT', MAILCHIMP_SUBJECT, ACTIVATE_SCRIPT)
    _set_environment_variable('MAILCHIMP_FROM_NAME', MAILCHIMP_FROM_NAME, ACTIVATE_SCRIPT)
    _set_environment_variable('MAILCHIMP_REPLY_TO', MAILCHIMP_REPLY_TO, ACTIVATE_SCRIPT)
    _set_environment_variable('PETPOINT_AUTH_KEY', PETPOINT_AUTH_KEY, ACTIVATE_SCRIPT)
    _set_environment_variable('WAGTAILADMIN_NOTIFICATION_FROM_EMAIL', WAGTAILADMIN_NOTIFICATION_FROM_EMAIL, ACTIVATE_SCRIPT)
    _set_environment_variable('FACEBOOK_PAGE_ACCESS_TOKEN', FACEBOOK_PAGE_ACCESS_TOKEN, ACTIVATE_SCRIPT)
    _set_environment_variable('TWITTER_CONSUMER_KEY', TWITTER_CONSUMER_KEY, ACTIVATE_SCRIPT)
    _set_environment_variable('TWITTER_CONSUMER_SECRET', TWITTER_CONSUMER_SECRET, ACTIVATE_SCRIPT)
    _set_environment_variable('TWITTER_ACCESS_TOKEN_KEY', TWITTER_ACCESS_TOKEN_KEY, ACTIVATE_SCRIPT)
    _set_environment_variable('TWITTER_ACCESS_TOKEN_SECRET', TWITTER_ACCESS_TOKEN_SECRET, ACTIVATE_SCRIPT)


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
    run('pg_dump -U ' + PROJECT_USER + ' ' + DB_NAME + ' > ~/backups/' + backup_name)


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
