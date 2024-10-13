from flasgger import Swagger
from src.settings import __env


def configure_swagger(app):
    """
    Configures Swagger for the given Flask app.

    Args:
        app (Flask): The Flask application instance.
    """
    title = app.config["SWAGGER_TITLE"]
    description = app.config["SWAGGER_DESCRIPTION"]
    version = app.config["SWAGGER_VERSION"]
    swagger_ui = app.config["SWAGGER_UI"]
    host = app.config["SWAGGER_HOST"]
    base_path = app.config["SWAGGER_BASE_PATH"]
    swagger_specs_route = app.config["SWAGGER_SPECS_ROUTE"]
    swagger_endpoint = app.config["SWAGGER_ENDPOINT"]
    swagger_route = app.config["SWAGGER_ROUTE"]
    swagger_static_url_path = app.config["SWAGGER_STATIC_URL_PATH"]

    swagger_security = app.config["SWAGGER_SECURITY"]
    security_definitions = app.config["SWAGGER_SECURITY_DEFINITIONS"]

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": swagger_endpoint,
                "route": swagger_route,
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": swagger_static_url_path,
        "swagger_ui": swagger_ui,
        "specs_route": swagger_specs_route,
    }

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": title,
            "description": description,
            "version": version,
        },
        "host": host,
        "basePath": base_path,
        "schemes": ["http", "https"],
        "securityDefinitions": (
            (security_definitions if security_definitions else {})
            if swagger_security
            else None
        ),
    }

    swagger = Swagger(app, config=swagger_config, template=swagger_template)
    return swagger
