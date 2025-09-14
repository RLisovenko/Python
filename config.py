import os
import secrets
from pathlib import Path

from decouple import config

FNAME_FLASK_SECRET_KEY = Path(".flask_secret")


def get_secret_key(fname_secret: str) -> str:

    secret_key = os.environ.get("FLASK_SECRET_KEY")

    if secret_key is None:
        try:
            with open(fname_secret, "r") as _file:
                secret_key = _file.read()
        except FileNotFoundError:
            with open(fname_secret, "w") as _file:
                print(f"Generation new SECRET_KEY. Check: {fname_secret}")
                secret_key = secrets.token_hex(32)
                _file.write(secret_key)
    else:
        with open(fname_secret, "w") as _file:
            _file.write(secret_key)

    return secret_key


class BaseConfig(object):

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = get_secret_key(os.path.join(BASEDIR, FNAME_FLASK_SECRET_KEY))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "db.sqlite3")


class ProductionConfig(BaseConfig):
    DEBUG = False
    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(
        config("DB_ENGINE", default="postgresql"),
        config("DB_USERNAME", default="postgresql"),
        config("DB_PASS", default="postgresql"),
        config("DB_HOST", default="localhost"),
        config("DB_PORT", default=5432),
        config("DB_NAME", default="postgresql-flask"),
    )


# Load all possible configurations
config_dict = {"Production": ProductionConfig, "Development": DevelopmentConfig}
