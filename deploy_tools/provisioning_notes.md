Provisioning a new site
================================

## Required packages:

* nginx
* Python 3.9
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python39 python3.9-venv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com
* replace SEKRIT with email password

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
