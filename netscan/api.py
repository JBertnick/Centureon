# netscan/api.py
# This API allows scan servers to submit results.

from tastypie.resources import ModelResource, fields, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from netscan.models import Device, Client_networks
from users.models import Client

class ClientResource(ModelResource):
    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        allowed_methods = ['get', 'post', 'put']

class Client_networksResource(ModelResource):
    client = fields.ForeignKey(ClientResource, 'client', full=True)
    class Meta:
        queryset = Client_networks.objects.all()
        resource_name = 'client_networks'
        allowed_methods = ['get', 'post', 'put']

        filtering = {
            'client': ALL_WITH_RELATIONS
        }

class DeviceResource(ModelResource):
    client = fields.ForeignKey(ClientResource, 'client', full=True)
    class Meta:
        queryset = Device.objects.all()
        resource_name = 'device'
        allowed_methods = ['get', 'post', 'put']
        authorization = Authorization()

        filtering = {
            'client': ALL_WITH_RELATIONS,
            'ip_address': ALL_WITH_RELATIONS
        }


