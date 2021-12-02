from flask import Flask
from auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)

    app.run()


if __name__ == "__main__":
    create_app()