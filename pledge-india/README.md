# Pledge-India

This repository contains all the source code related to the project `pledge-india` under the license GPLv3+.

## Introduction

## Features

## Technologies used

This project runs on Python3 and Django 2. Other Python Libraries used can be found in `requirements`.

Database used: `PostgresSQL`

Frontend Framework: `Bootstrap v4`

## How to setup?

Create a Python3 Virtual Environmentm, activate it and install the development requirements from `requirements/local.txt`

```
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements/local.txt --user
```
Navigate to `pledgeindia/pledgeindia` and create .env file with following:

```
DEBUG=True
DJANGO_SECRET=<Some_long_random_string>
DATABASE_PORT=5432
DATABASE_HOST=localhost
DATABASE_NAME=<DATABASE_NAME>
DATABASE_USER=<DATABASE_USER>
DATABASE_PASS=<DATABASE_PASS>

# social login
FACEBOOK_APP_ID=''
FACEBOOK_APP_SECRET=''
```


Navigate to `pledgeindia`, and apply any pending migrations by running `python manage.py migrate`. Now, Start the development server by `python manage.py runserver 0.0.0.0:8000`

## Contributors
- @tucosaurus 
- @thisisayush
- @utkarsh2102
- @vipulgupta2048
