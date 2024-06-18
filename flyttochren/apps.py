from django.apps import AppConfig


class ForConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flyttochren'

    def ready(self):
        import flyttochren.signals