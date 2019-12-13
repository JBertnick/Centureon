from django.contrib import admin
from .models import sites, assets_owners, assets_tags, assets_networks, assets_virtualappliance, assets_clouds, assets_datastores, assets_hosts, assets_master, assets_users, assets_ports

admin.site.register(sites)
admin.site.register(assets_owners)
admin.site.register(assets_tags)
admin.site.register(assets_networks)
admin.site.register(assets_virtualappliance)
admin.site.register(assets_clouds)
admin.site.register(assets_datastores)
admin.site.register(assets_hosts)
admin.site.register(assets_master)
admin.site.register(assets_users)
admin.site.register(assets_ports)

