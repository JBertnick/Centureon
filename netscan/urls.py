from django.conf.urls import url, include
from django.urls import path
from netscan.api import ClientResource
from netscan.views import assetsview, devicesview, datastoresview, cloudsview, usersview, networksview, sitesview, devicesdetailedview, sitedetailedview, deviceaddview, useraddview, devicedeleteview
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(ClientResource())

urlpatterns = [url(r'^api/', include(v1_api.urls)),
    path('home/assets', assetsview),
    path('home/assets/devices', devicesview),
    path('home/assets/datastores', datastoresview),
    path('home/assets/clouds', cloudsview),
    path('home/assets/users', usersview),
    path('home/assets/networks', networksview),
    path('home/assets/sites', sitesview),
    path('home/assets/devices/<int:id>/', devicesdetailedview),
    path('home/assets/sites/<int:id>/', sitedetailedview),
    path('home/assets/devices/add/', deviceaddview),
    path('home/assets/devices/<int:id>/delete', devicedeleteview),
    path('home/assets/users/add/', useraddview),
    #path('home/company/assets/update-host', update_assets_host, name='updatehosts'),
    #path('home/company/assets/new-host', new_assets_host, name='newhosts')
    ]