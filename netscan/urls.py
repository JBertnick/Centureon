from django.conf.urls import url, include
from django.urls import path
from netscan.api import ClientResource
from netscan.views import assetsview, devicesview, datastoresview, cloudsview, usersview, networksview, sitesview, devicesdetailedview, sitedetailedview, deviceaddview, useraddview, userdetailedview, siteaddview, datastoreaddview, datastoredetailedview, cloudaddview, clouddetailedview, networkdetailedview, networkaddview
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(ClientResource())

urlpatterns = [url(r'^api/', include(v1_api.urls)),
    path('home/assets', assetsview),
    path('home/assets/devices', devicesview),
    path('home/assets/datastores', datastoresview),
    path('home/assets/clouds', cloudsview),
    path('home/assets/clouds/<int:id>/', clouddetailedview),
    path('home/assets/clouds/add/', cloudaddview),
    path('home/assets/clouds/edit/<int:id>/', cloudaddview),
    path('home/assets/users', usersview),
    path('home/assets/networks', networksview),
    path('home/assets/networks/<int:id>/', networkdetailedview),
    path('home/assets/networks/add/', networkaddview),
    path('home/assets/networks/edit/<int:id>/', networkaddview),
    path('home/assets/sites', sitesview),
    path('home/assets/sites/add/', siteaddview),
    path('home/assets/devices/<int:id>/', devicesdetailedview),
    path('home/assets/sites/<int:id>/', sitedetailedview),
    path('home/assets/devices/add/', deviceaddview),
    path('home/assets/users/add/', useraddview),
    path('home/assets/users/<int:id>/', userdetailedview),
    path('home/assets/datastores/add/', datastoreaddview),
    path('home/assets/datastores/<int:id>/', datastoredetailedview),
    #path('home/company/assets/update-host', update_assets_host, name='updatehosts'),
    #path('home/company/assets/new-host', new_assets_host, name='newhosts')
    ]