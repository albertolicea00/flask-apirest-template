from flask import Blueprint, request, jsonify
from src.blueprints import __bp_name__

# import modules, actions, services here ...

bp = Blueprint(__bp_name__(), __name__, url_prefix="/")


@bp.route("/", methods=["GET"], strict_slashes=False)
def test_self():
    """
    Endpoint returning a example simple JSON response.
    ---
    responses:
      200:
        description: A successful response
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Hello World"
    """
    return jsonify({"message": "Hello World"}), 200
