import logging
import logging.config
import os
from os import environ
from sys import exit

from helpers import get_app_config, get_target_server, init_env

init_env()
target_server = get_target_server()
app_config = get_app_config(target_server)

from app.app import create_app

app = create_app(app_config)

if __name__ == "__main__":
    # app.run(use_reloader=True)
    app.run(host="127.0.0.1", port=5151, debug=True, use_reloader=True)
