from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver 
from django.contrib.contenttypes.models import ContentType
from netscan.models import assets_hosts, assets_networks, assets_master
    
@receiver(post_save, sender=assets_hosts)
@receiver(post_save, sender=assets_networks)
def save_host(sender, instance, created, **kwargs):
    if created:
        type = ContentType.objects.get_for_model(instance.__class__)
        assets_master.objects.get_or_create(type=type, object_id=instance.id, name=instance.name, client=instance.client, created_by=instance.created_by)
