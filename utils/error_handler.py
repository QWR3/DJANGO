from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from constants.constants import ResponseConstants


def custom_exception_handler(exc, content):
    handler = {
        'JwtException': _jwt_validate_error
    }
    exc_class = exc.__class__.__name__
    if exc_class in handler:
        handler[exc_class](exc, content)
    return exception_handler(exc, content)


def _jwt_validate_error(exc, content) -> Response:
    return Response(ResponseConstants.bad_request.msg, ResponseConstants.bad_request.status)
