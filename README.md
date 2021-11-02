# sfpassman

Set random generated snowflake user passwords and store them in AWS Secrets Manager

## Usage

```
usage: sfpassman [-h] target_user secret_id admin_user account region

Set a snowflake user's password in both secrets manager + snowflake to a
random string.

positional arguments:
  target_user  Snowflake target user (to set password for)
  secret_id    Secret ID for storing in Secret Manager
  admin_user   Snowflake admin user (used to set the password)
  account      Snowflake account
  region       Snowflake user

optional arguments:
  -h, --help   show this help message and exit

Admin user password is expected in the env var SNOWFLAKE_PASSWORD.
```

Example:

```
sfpassman snowflakeuser/PROD_JAFFLES_SA admin TX12345 ap-southeast-2
```

## Development

### Prerequisites

- make
- node (required for pyright. Install via `brew install node`)
- python >= 3.7

### Getting started

To get started run `make install`. This will:

- install git hooks for formatting & linting on git push
- create the virtualenv in _.venv/_
- install this package in editable mode

Then run `make` to see the options for running checks, tests etc.

`. .venv/bin/activate` activates the virtualenv. When the requirements in `setup.py` change, the virtualenv is updated by the make targets that use the virtualenv.
