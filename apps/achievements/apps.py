from django.apps import AppConfig


class AchievementsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.achievements'
    verbose_name = 'Conquistas'
    
    def ready(self):
        # Importa os signals
        from . import services  # noqa
