from django.apps import AppConfig


class ConfappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'confapp'
    verbose_name = 'Основное приложение для конфигурации' 