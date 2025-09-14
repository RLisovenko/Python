import logging
import logging.config
import os


def get_target_server() -> str:

    TARGET_SERVER = os.environ.get("TARGET_SERVER") or "development"
    SERVER_MODES = ("development", "production")
    if TARGET_SERVER.lower() not in SERVER_MODES:
        print(f"Error: Invalid <TARGET_SERVER> environmental value. Expected values:{SERVER_MODES}")
        TARGET_SERVER = "development"
    return TARGET_SERVER


def get_app_config(target_server) -> dict:

    app_config = None
    if target_server.lower() == "development":
        from config import DevelopmentConfig

        app_config = DevelopmentConfig
        logging.config.fileConfig("configs-logging/logging.conf")

    if target_server.lower() == "production":
        from config import ProductionConfig

        app_config = ProductionConfig
        logging.config.fileConfig("configs-logging/logging-prod.conf")

    return app_config


def init_env() -> None:
    """Initiate working environment"""
    LOGS_FOLDER = ".logs"
    if not os.path.exists(LOGS_FOLDER):
        os.makedirs(LOGS_FOLDER)
