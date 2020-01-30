from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver 
from users.models import CustomUser
    
@receiver(post_save, sender=CustomUser)
def create_apikey(sender, instance, **kwargs):
    if instance.is_api is True:
        from tastypie.models import create_api_key
        create_api_key(sender, instance, **kwargs)

