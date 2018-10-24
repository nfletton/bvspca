#!/usr/bin/env bash
cd /home/vagrant/bowvalleyspca_org
pip freeze | grep -v \"^-e\" | xargs pip uninstall -y; pip uninstall -y setuptools; pip install setuptools
pip install -U pip; pip install -U setuptools; pip install -r /home/vagrant/canmoreskirentals_com/requirements/local.txt
./manage.py collectstatic --noinput
./manage.py migrate --noinput
