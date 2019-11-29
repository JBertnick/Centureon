from django.conf.urls import url, include
from django.urls import path
from webportal.views import homeview, companyview, adduserview, kibanaview, zscalerview, solarwindsview, companyassetsview, companysitesview, companynetworksview, sentienloneview, auroraproxyview, companyusersview
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    ##path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    url('proxy/(?P<path>.*)$', auroraproxyview.as_view()),
    path('home/', homeview),
    path('home/company/kibana', kibanaview),
    path('home/company/zscaler', zscalerview),
    path('home/company/solarwinds', solarwindsview),
    path('home/company/sentinelone', sentienloneview),
    path('home/company/assets', companyassetsview),
    path('home/company/users', companyusersview),
    path('home/company/networks', companynetworksview),
    path('home/company/sites', companysitesview),
    path('home/company', companyview, name='companyprofile'),
    path('home/company/adduser', adduserview, name='adduser')
]