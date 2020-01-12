from django.conf.urls import url, include
from django.urls import path
from webportal.views import homeview, companyview, adduserview, kibanaview, zscalerview, solarwindsview, sentienloneview, usersview
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    ##path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', homeview),
    path('home/company/kibana', kibanaview),
    path('home/company/zscaler', zscalerview),
    path('home/company/solarwinds', solarwindsview),
    path('home/company/sentinelone', sentienloneview),
    path('home/company', companyview, name='companyprofile'),
    path('home/company/users', usersview),
    path('home/company/adduser', adduserview, name='adduser')
]