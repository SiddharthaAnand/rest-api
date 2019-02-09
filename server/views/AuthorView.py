from flask import request, json, Response, Blueprint, g


author_api = Blueprint('author_api', __name__)


@author_api.route('', methods=["GET"])
def get_author():
    """

    :return:
    """
    pass


@author_api.route('/<author_name>', methods=["GET"])
def get_author_information(author_name):
    """

    :return:
    """
    return custom_response({'author_name': author_name}, 200)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
