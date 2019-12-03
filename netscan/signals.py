from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from netscan.models import assets_hosts, assets_master
    
@receiver(pre_save, sender=assets_hosts)
def save_host(sender, instance, **kwargs):
    host_profile = assets_master.object.create(type='assets_hosts', object_id=kwargs['instance'])
