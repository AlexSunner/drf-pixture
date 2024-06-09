from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from datetime import datetime, timezone
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
)

@api_view(['POST'])
def logout_route(request):
    response = Response()
    expires = datetime(1970, 1, 1, tzinfo=timezone.utc)

    response.set_cookie(
        key=settings.JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires=expires,
        max_age=0,
        samesite=settings.JWT_AUTH_SAMESITE,
        secure=settings.JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=settings.JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires=expires,
        max_age=0,
        samesite=settings.JWT_AUTH_SAMESITE,
        secure=settings.JWT_AUTH_SECURE,
    )
    return response

@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to my drf API!"
    })
