from flask import Flask

from routes import router
from config import mongo


def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb+srv://admin:6iKyAiPFT9JAabB8@cluster0.9ck3e.mongodb.net/mydb?retryWrites=true&w=majority'

    mongo.init_app(app)

    app.register_blueprint(router)
    app.run()


if __name__ == "__main__":
    create_app()