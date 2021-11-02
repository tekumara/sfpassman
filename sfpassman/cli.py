import argparse
import os
import sys
from typing import List

from sfpassman import set_random_password


def argpaser() -> argparse.ArgumentParser:
    desc = """
        Set a snowflake user's password in both secrets manager + snowflake to a random string.
    """
    epilog = """
        Admin user password is expected in the env var SNOWFLAKE_PASSWORD.
    """
    parser = argparse.ArgumentParser(description=desc, epilog=epilog)
    parser.add_argument("target_user", type=str, help="Snowflake target user (to set password for)")
    parser.add_argument("secret_id", type=str, help="Secret ID for storing in Secret Manager")
    parser.add_argument("admin_user", type=str, help="Snowflake admin user (used to set the password)")
    parser.add_argument("account", type=str, help="Snowflake account")
    parser.add_argument("region", type=str, help="Snowflake user")
    return parser


def read_env_var(name: str) -> str:
    value = os.environ.get(name, None)

    if not value:
        raise EnvironmentError(f"Missing environment variable {name}")

    return value


def main(args: List[str] = sys.argv[1:]) -> None:
    parser = argpaser()
    parsed = parser.parse_args(args)

    admin_password = read_env_var("SNOWFLAKE_PASSWORD")

    set_random_password(
        parsed.target_user, parsed.secret_id, parsed.admin_user, admin_password, parsed.account, parsed.region
    )


if __name__ == "__main__":
    main()
