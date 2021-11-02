import logging
import os
import secrets
import string

import boto3
import snowflake.connector
from snowflake.connector import SnowflakeConnection

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


def set_random_password(
    target_user: str, secret_id: str, admin_user: str, admin_password: str, account: str, region: str
) -> None:
    logging.info(f"Snowflake: connecting to {account}.{region} as user {admin_user}")

    # use server-side binding to correctly quote any punctuation in the password
    # and to avoid the password appearing in the logs
    snowflake.connector.paramstyle='qmark'

    conn = snowflake.connector.connect(
        user=admin_user,
        role="SECURITYADMIN",
        password=admin_password,
        account=account,
        region=region,
        session_parameters={
            "QUERY_TAG": "sfpassman",
        },
    )

    pw = generate_random_password()

    logging.info(f"Secrets Manager: setting secret {secret_id}")
    sm_put_secret(secret_id, pw)

    logging.info(f"Snowflake: Setting password for {target_user}")
    sf_set_password(conn, target_user, pw)

    logging.info("Success 🎉")


def generate_random_password() -> str:
    alphabet = string.digits + string.ascii_letters + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(32))


def sm_put_secret(id: str, value: str) -> None:
    aws_region = os.environ.get("AWS_DEFAULT_REGION")
    secretsmanager = boto3.client("secretsmanager", region_name=aws_region)
    secretsmanager.put_secret_value(
        SecretId=id,
        SecretString=value,
    )


def sf_set_password(conn: SnowflakeConnection, user: str, password: str) -> None:
    conn.cursor().execute(f"ALTER USER {user} SET PASSWORD = ?", (password,))
