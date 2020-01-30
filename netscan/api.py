# netscan/api.py
# This API allows scan servers to submit results.

from tastypie.resources import ModelResource, fields, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from users.models import Client, CustomUser
from netscan.models import assets_networks, assets_hosts, assets_ports

class ClientResource(ModelResource):
    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        allowed_methods = ['get', 'post']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(client=bundle.request.user.client)
    
    def obj_create(self, bundle, **kwargs):
        return super(MyModelResource, self).obj_create(bundle, client=bundle.request.user.client)

class Client_networks(ModelResource):
    class Meta:
        queryset = assets_networks.objects.all()
        resource_name = 'networks'
        allowed_methods = ['get', 'post', 'put']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(client=bundle.request.user.client)
    
    def obj_create(self, bundle, **kwargs):
        return super(MyModelResource, self).obj_create(bundle, client=bundle.request.user.client)

class Client_device(ModelResource):
    class Meta:
        queryset = assets_hosts.objects.all()
        resource_name = 'devices'
        allowed_methods = ['get', 'post', 'put']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()
        excludes = ['created_at', 'description', 'external_asset', 'name', 'valid_until']

        filtering = {
            'ip_address': ALL_WITH_RELATIONS,
        }

    def authorized_read_list(self, object_list, bundle):
        return object_list.filter(client=bundle.request.user.client)
    
    def obj_create(self, bundle, **kwargs):
        return super(Client_device, self).obj_create(bundle, client=bundle.request.user.client)

class Device_ports(ModelResource):
    class Meta:
        queryset = assets_ports.objects.all()
        resource_name = 'ports'
        allowed_methods = ['get', 'post', 'put']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()

        filtering = {
            'type': ALL_WITH_RELATIONS,
            'number': ALL_WITH_RELATIONS,
        }

class Users(ModelResource):
    class Meta:
        queryset = CustomUser.objects.all()
        resource_name = 'User'
        allowed_methods = ['get', 'post', 'put']
        authentication = ApiKeyAuthentication()


