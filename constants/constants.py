from enum import Enum

from rest_framework import status


class ResponseConstants(Enum):
    ok = ('', status.HTTP_200_OK)
    created = ('', status.HTTP_201_CREATED)
    bad_request = ('token invalid or expired', status.HTTP_400_BAD_REQUEST)

    def __init__(self, msg, status) -> None:
        self.msg = msg
        self.status = status
