from django.conf.urls import url, include
from django.urls import path
from netscan.api import ClientResource, DeviceResource, Client_networksResource
from netscan.views import update_assets_host, new_assets_host
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(ClientResource())
v1_api.register(DeviceResource())
v1_api.register(Client_networksResource())

urlpatterns = [url(r'^api/', include(v1_api.urls)),
    path('home/company/assets/update-host', update_assets_host, name='updatehosts'),
    path('home/company/assets/new-host', new_assets_host, name='newhosts')
    ]