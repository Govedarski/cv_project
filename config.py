from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import Routes


class ProductionConfiguration:
    FLASK_ENV = "ProductionConfiguration"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@{config('DB_URL')}:{config('DB_PORT')}/{config('DB_NAME')}"
    )


class DevelopmentConfiguration:
    FLASK_ENV = "DevelopmentConfiguration"
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@{config('DB_URL')}:{config('DB_PORT')}/{config('DB_NAME')}"
    )


class TestingConfiguration:
    FLASK_ENV = "TestConfiguration"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@{config('DB_URL')}:{config('DB_PORT')}/{config('TEST_DB_NAME')}")


def create_app(configuration=None):
    # In development .env CONFIGURATION=config.DevelopmentConfiguration
    # In production .env CONFIGURATION=config.ProductionConfiguration
    # In test create_app param = config.TestingConfiguration
    app = Flask(__name__)
    # TODO: Add oauth
    # oauth.init_app(app)
    # app.secret_key = config("APP_SECRET_KEY") # for Google auth
    # TODO: or
    configuration = configuration or config("CONFIGURATION")
    app.config.from_object(configuration)

    api = Api(app)
    Migrate(app, db)
    db.init_app(app)

    CORS(app)

    [api.add_resource(*route.values()) for route in Routes.values()]
    return app
