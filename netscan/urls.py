from django.conf.urls import url, include
from netscan.api import ClientResource, DeviceResource, Client_networksResource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(ClientResource())
v1_api.register(DeviceResource())
v1_api.register(Client_networksResource())

urlpatterns = [url(r'^api/', include(v1_api.urls))]