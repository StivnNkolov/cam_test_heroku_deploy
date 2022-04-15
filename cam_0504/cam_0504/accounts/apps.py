from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cam_0504.accounts'

    def ready(self):
        from . import signals
