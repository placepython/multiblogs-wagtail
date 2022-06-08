from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "multiblogs.users"
    label = "users"
    verbose_name = _("Users")

    def ready(self):
        try:
            from . import signals  # noqa F401
        except ImportError:
            pass
