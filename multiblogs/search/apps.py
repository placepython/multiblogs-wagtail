from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SearchConfig(AppConfig):
    name = "multiblogs.search"
    label = "search"
    verbose_name = _("Search")

    def ready(self):
        try:
            from . import signals  # noqa F401
        except ImportError:
            pass
