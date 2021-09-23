from datetime import timedelta

from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import AccessToken, BlacklistMixin

from exceptions.jwt_exception import JwtException


class _AccessToken(BlacklistMixin, AccessToken):
    lifetime = timedelta(hours=1)


class JwtUtils:
    @staticmethod
    def create_activated_token(user):
        return _AccessToken.for_user(user)

    @staticmethod
    def validate_token(token):
        try:
            access_token = _AccessToken(token)
            if not OutstandingToken.objects.filter(token=token).exists():
                raise JwtException
            access_token.check_blacklist()
            access_token.blacklist()
        except Exception:
            raise JwtException
