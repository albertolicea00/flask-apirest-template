# Flask API Server Template 🚀
A streamlined template for quickly setting up a Flask-based server. Includes essential configurations, **CORS** setup, blueprint registration, and **Swagger integration** for API documentation. Features a **folder-based routing system** and a **scalable architectur**e, making it ideal for building and maintaining **RESTful APIs**. Additionally, it includes extra functions like **serializers** to convert objects into simple returnable JSONs.

## 🌳 File Structure

```bash
├───src/
│   ├───helpers/        # Utility functions and helper methods
│   │   └─── ...
│   ├───router/         # Route definitions and handlers
│   │   └─── ...
│   ├───middleware/     # Middleware functions for request/response processing
│   │   └─── ...
│   ├───services/       # Vendor logic and service layer
│   │   └─── ...
│   │
│   ├───blueprints.py   # Blueprint definitions for modularizing routes
│   ├───config.py       # Configuration settings for the application (++env)
│   ├───settings.py     # Configuration environment settings for the application
│   ├───setup.py        # Setup script for initializing the application
│   └───swagger.py      # Swagger documentation setup
│
├───tests/              # Test cases and testing framework folder
│   ├───router/         # Tests for route handlers
│   │   └─── ...
│   └─── ...
│
├───Dockerfile          # Instructions for building the Docker image
├───.env                # Environment variables for the **application**
└───app.py              # Main application entry point
```

- Each endpoint of the application must be placed within the router directory and follow the naming convention `__route_name__.py` or just `__route.py`.
- Additionally, each endpoint should be contained within a parent folder and include the following code snippet:

```python
# `router > parent_folder_name > endpoint_name`
from flask import Blueprint, jsonify
from src.blueprints import __bp_name__
bp = Blueprint(__bp_name__(), __name__, url_prefix="/parent_folder_name")
...
```

Furthermore, each endpoint must be isolated (**only one endpoint per file**) with the following structure

```python
...
@bp.route("/endpoint_name", methods=["METHODS_TYPE"], strict_slashes=False)
def endpoint_name():
    return jsonify({"message": "Example Response"}), 200
```

## ⚠️ Code Style

- use [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) to comply to our code formatting standard. This will make the job easier for the reviewers of pull requests; you can use `# fmt: off` and `# fmt: on` to prevent formatting the code between these two comments (not recommended)

- Add swagger docstring for new features with the following structure:

```python
@bp.route("/hello_word", methods=["GET"], strict_slashes=False)
def hello_word():
    """
    Endpoint returning a simple Hello world JSON message.
    ---
    tags:
      - Example
    responses:
      200:
        description: A successful response
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Hello world"
    """
    return jsonify({"message": "Hello world"}), 200
```

- Ensure compliance swagger with the [OpenAPI v3 Specifications](https://swagger.io/specification/v3/).

- Add tests for new features in the `tests/` directory.

  - ..

- <!-- TODO -->

# 📂 How to Implement

1. **Clone the Repository**: Clone the repository to your local machine using:

   ```bash
   git clone https://github.com/Nitza-Developement/pz-kb-server.git
   ```

# 📦 Docker's Commands

## Prerequisites

1. You need to have [Docker](https://docs.docker.com/) installed on your machine.

### Build the image

```bash
docker build -t flask-apirest-server .
```

### Create **container**

```bash
docker run --name flask-apirest-container -d -p 5000:5000 flask-apirest-server
```

<!-- Build & Create dev container  -->
<!-- docker build -t flask-apirest-container . && docker run --name flask-apirest-server -d -p 5000:5000 flask-apirest-container -->

### Run container

```bash
docker run flask-apirest-container
```

### Shell inside container

```bash
docker exec -it flask-apirest-container /bin/sh
```

### Stop container

```bash
docker stop flask-apirest-server
```

### Remove container

```bash
docker rmi flask-apirest-container
```

# ↪️ Commands inside container

### run server

```bash
flask run
```

### run tests

```bash

```

## Reporting Issues

If you find a bug or have a suggestion, please open an [issue](https://github.com/albertolicea00/flask-apirest-template/issues). Provide as much detail as possible to help us understand and address the issue.

Thank you for your contributions! 😃
