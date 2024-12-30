from django.apps import AppConfig
import os

class AdopcionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adopcion'
    path = os.path.dirname(os.path.abspath(__file__))
