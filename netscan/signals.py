from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver 
from django.contrib.contenttypes.models import ContentType
from netscan.models import assets_hosts, assets_networks, assets_master, assets_clouds, assets_datastores, assets_users, assets_virtualappliance
from users.models import CustomUser
import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Saving Assets and updating master record
@receiver(post_save, sender=assets_hosts)
@receiver(post_save, sender=assets_networks)
@receiver(post_save, sender=assets_clouds)
@receiver(post_save, sender=assets_datastores)
@receiver(post_save, sender=assets_users)
def save_asset(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(instance.__class__)
        assets_master.objects.get_or_create(content_type=content_type, object_id=instance.id, name=instance.name, client=instance.client, created_by=instance.created_by)

# Create a VA Scanner!
@receiver(post_save, sender=assets_virtualappliance)
def save_va(sender, instance, created, **kwargs):
    if created:
        email = str(instance.id) + '@vascanner.com'
        password = randomString()
        CustomUser.objects.get_or_create(email=email, password=password, is_api=True, client=instance.client)
        user = CustomUser.objects.get(email=email)
        instance.login = user
        instance.save()

# Delete a VA Scanner!
@receiver(post_delete, sender=assets_virtualappliance)
def delete_va(sender, instance, **kwargs):
    user = instance.login
    user.delete()

@receiver(post_delete, sender=assets_hosts)
@receiver(post_delete, sender=assets_networks)
@receiver(post_delete, sender=assets_clouds)
@receiver(post_delete, sender=assets_datastores)
@receiver(post_delete, sender=assets_users)
def delete_asset(sender, instance, **kwargs):
    content_type = ContentType.objects.get_for_model(instance.__class__)
    assets_master.objects.filter(content_type=content_type, object_id=instance.id).delete()

@receiver(post_delete, sender=assets_master)
def delete_asset(sender, instance, **kwargs):
    if str(instance.content_type) == 'assets_hosts':
       assets_hosts.objects.filter(pk=instance.object_id).delete()
    elif str(instance.content_type) == "assets_networks":
        assets_networks.objects.filter(pk=instance.object_id).delete()
    elif str(instance.content_type) == 'assets_clouds':
        assets_clouds.objects.filter(pk=instance.object_id).delete()
    elif str(instance.content_type) == 'assets_datastores':
        assets_datastores.objects.filter(pk=instance.object_id).delete()
    elif str(instance.content_type) == 'assets_users':
        assets_users.objects.filter(pk=instance.object_id).delete()
    else:
        pass

    
    
    
   