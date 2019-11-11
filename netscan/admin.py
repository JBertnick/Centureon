from django.contrib import admin
from .models import Enginer
from .models import Device
from .models import Agent
from .models import Scan_data
from .models import Client_networks

admin.site.register(Enginer)
admin.site.register(Device)
admin.site.register(Agent)
admin.site.register(Scan_data)
admin.site.register(Client_networks)
