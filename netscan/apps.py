from django.apps import AppConfig

class NetscanConfig(AppConfig):
    name = 'netscan'
    
    def ready(self):
        import netscan.signals

