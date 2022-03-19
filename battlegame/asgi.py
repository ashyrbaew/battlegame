"""
ASGI config for battlegame project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "battlegame.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

from mainapp.consumers import *

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": django_asgi_app,

    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^battles_create/$", MainappConsumer.as_asgi()),
            # url(r"^battles_list/$", ListConsumer.as_asgi()),
            # url(r"^battles/accept/$", AcceptConsumer.as_asgi()),
            # url(r"^battles_start/$", StartConsumer.as_asgi()),
            # url(r"^battles_move/$", MoveConsumer.as_asgi()),
            # url(r"^battles_finish/$", ResultConsumer.as_asgi()),
        ])
    ),
})