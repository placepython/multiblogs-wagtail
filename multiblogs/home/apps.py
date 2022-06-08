from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HomeConfig(AppConfig):
    name = "multiblogs.home"
    label = "home"
    verbose_name = _("Home")

    def ready(self):
        try:
            from . import signals  # noqa F401
        except ImportError:
            pass
