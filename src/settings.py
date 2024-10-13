# fmt: off
import os
from collections import UserDict
from dotenv import load_dotenv
load_dotenv()

class EnvDict(UserDict):
    """
    EnvConfig allowing easy access to configuration variables using dictionary-like syntax.

    It returns the value of a config variable if it exists, and returns None
    if the variable is not defined in the Flask config.

    Usage:
        __env["EXISTING_KEY"]  # Returns the value of the config key
        __env["NON_EXISTING_KEY"]  # Returns None if the key doesn't exist
    """

    def __getitem__(self, key):
        return self.data.get(key, None)


# Instance of EnvConfig for direct use
__env = EnvDict(
    {
        # APP
        "DEBUG": os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1"),
        "HOST": os.getenv("FLASK_HOST", "0.0.0.0"),
        "PORT": os.getenv("FLASK_PORT", "5000"),
        "SERVER": f"{os.getenv('FLASK_PROTOCOL', 'http')}://{os.getenv('FLASK_HOST', '0.0.0.0')}:{os.getenv('FLASK_PORT', '5000')}",
        "SECRET_KEY": os.getenv("SECRET_KEY"),
        "ENV": os.getenv("FLASK_ENV", "development"),
        "CORS_ORIGINS": "*",
        "CORS_ALLOW_HEADERS": ["Authorization", "Content-Type"],
        "CORS_EXPOSE_HEADERS": ["Authorization"],
        "CORS_SUPPORTS_CREDENTIALS": True,
        "CORS_METHODS": ["GET", "POST", "OPTIONS"],

        # ROUTER
        "ROUTER_DIR": "router",
        "ROUTES_FILES": [
            "routes.py",
            "route.py",
            "urls.py",
            "url.py",
        ],
        "ROUTES_FILES_BETWEEN": [
            ("__", ".py"),
        ],
        "ROUTES_FILES_IGNORE": [
            "__init__.py",
        ],

        # SWAGGER
        "SWAGGER_UI": os.getenv("SWAGGER_UI", "True").lower() in ("true", "1"),
        "SWAGGER_HOST": os.getenv("SWAGGER_HOST", "localhost:5000"),
        "SWAGGER_TITLE" : "Example swagger title",
        "SWAGGER_DESCRIPTION" : "Example swagger description",
        "SWAGGER_VERSION" : "1.0.0",
        "SWAGGER_BASE_PATH": "/",
        "SWAGGER_SPECS_ROUTE": "/apidocs/",
        "SWAGGER_ENDPOINT": "apispec",
        "SWAGGER_ROUTE": "/apispec.json",
        "SWAGGER_STATIC_URL_PATH": "/flasgger_static",

        "SWAGGER_SECURITY" : False,
        "SWAGGER_SECURITY_DEFINITIONS" : {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer {token}"',
            }, 
        },
        # include more global env settings here ...
    }
)
