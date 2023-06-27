from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication


class CustomAuthentication(JWTAuthentication, SessionAuthentication):
    pass