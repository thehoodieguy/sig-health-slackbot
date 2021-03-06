"""
ASGI config for sig_health_slackbot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from django_project.sentry import sentry_init

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings.live")

application = get_asgi_application()


sentry_init()
