from flask import Blueprint, request, jsonify
from src.blueprints import __bp_name__
import os

bp = Blueprint(__bp_name__(), __name__, url_prefix="/example")


@bp.route("/1", methods=["PUT"], strict_slashes=False)
def test_self():
    """
    Endpoint returning a example simple JSON response.
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
              example: "Hello World, example 1"
    """
    return jsonify({"message": "Hello World, example 1"}), 200
