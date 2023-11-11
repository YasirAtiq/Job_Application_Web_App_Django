from django.apps import AppConfig


class JobApplicationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'job_application'

    def ready(self):
        import job_application.views
