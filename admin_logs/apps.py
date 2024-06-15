from django.apps import AppConfig

class AdminLogsConfig(AppConfig):
    name = 'admin_logs'

    def ready(self):
        import admin_logs.signals