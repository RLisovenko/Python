from flask import Flask


def create_app(config):

    app = Flask(__name__)
    app.config.from_object(config)

    from .todo import todo as todo_blueprint

    app.register_blueprint(todo_blueprint)

    return app
