def configure_cors(app):
    """
    Ensure all responses have the CORS headers. This ensures any failures are also accessible by the client.

    Args:
        app (Flask): The Flask application instance.
    """
    from flask_cors import CORS

    CORS(
        app,
        resources={
            r"/*": {
                "origins": app.config["CORS_ORIGINS"],
                "allow_headers": app.config["CORS_ALLOW_HEADERS"],
                "expose_headers": app.config["CORS_EXPOSE_HEADERS"],
                "supports_credentials": app.config["CORS_SUPPORTS_CREDENTIALS"],
                "methods": app.config["CORS_METHODS"],
            }
        },
    )


def configure_app(app):
    """
    Configures the Flask application with environment variables.

    Args:
        app (Flask): The Flask application instance.

    """
    from src.settings import __env

    for key, value in __env.items():
        app.config[key] = value
