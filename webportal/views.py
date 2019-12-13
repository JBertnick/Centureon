from django.shortcuts import render, redirect
from users.models import Client, CustomUser
from netscan.models import sites, assets_master
from django.contrib.auth import login, authenticate
from users.forms import CompanyAddUserForm
from django.contrib.auth.decorators import login_required
from revproxy.views import ProxyView

def homeview(request):
    if request.user.is_authenticated:
        client = request.user.client
    else:
        client = ''
        pass
     
    args = {'client': client}
    return render(request, 'home.html', args)

@login_required(login_url='/login/')
def kibanaview(request):
    if request.user.is_authenticated:
        client = request.user.client
    else:
        client = ''
        pass
     
    args = {'client': client}
    return render(request, 'kibana.html', args)

@login_required(login_url='/login/')
def sentienloneview(request):
    if request.user.is_authenticated:
        client = request.user.client
    else:
        client = ''
        pass
     
    args = {'client': client}
    return render(request, 'sentinelone.html', args)

@login_required(login_url='/login/')
def zscalerview(request):
    if request.user.is_authenticated:
        client = request.user.client
    else:
        client = ''
        pass
     
    args = {'client': client}
    return render(request, 'zscaler.html', args)

@login_required(login_url='/login/')
def solarwindsview(request):
    if request.user.is_authenticated:
        client = request.user.client
    else:
        client = ''
        pass
     
    args = {'client': client}
    return render(request, 'solarwinds.html', args)

@login_required(login_url='/login/')
def companyview(request):
    if request.user.is_authenticated:
        client = request.user.client
        head_office = sites.objects.filter(client=client, is_headoffice=True)
        for office in head_office:
            pass
    else:
        client = ''
        pass
    args = {'client': client, 'head_office': office}
    return render(request, 'company.html', args)

@login_required(login_url='/login/')
def companyusersview(request):
    if request.user.is_authenticated:
        client = request.user.client
        users = CustomUser.objects.filter(client=client)
    else:
        client = ''
        users = ''
        pass
    args = {'client': client, 'users': users}
    return render(request, 'company-users.html', args)

@login_required(login_url='/login/')
def companynetworksview(request):
    if request.user.is_authenticated:
        client = request.user.client
        networks = Client_networks.objects.filter(client=client)
    else:
        client = ''
        networks = ''
        pass
    args = {'client': client, 'networks': networks}
    return render(request, 'company-networks.html', args)

@login_required(login_url='/login/')
def companysitesview(request):
    if request.user.is_authenticated:
        client = request.user.client
        sites = sites.objects.filter(client=client)
    else:
        client = ''
        sites = ''
        pass
    args = {'client': client, 'sites': sites}
    return render(request, 'company-sites.html', args)

@login_required(login_url='/login/')
def companyassetsview(request):
    if request.user.is_authenticated:
        client = request.user.client
        assets = assets_master.objects.filter(client=client)
    else:
        client = ''
        pass
    args = {'client': client, 'assets': assets}
    return render(request, 'company-assets.html', args)

@login_required(login_url='/login/')
def adduserview(request):
    if request.user.is_authenticated:
        client = request.user.client
    else:
        client = ''
        pass
    initial_data = {
        'client': client,
    }
    form = CompanyAddUserForm(request.POST or None, initial=initial_data)
    return render(request, 'newuser.html', {'form': form})

class auroraproxyview(ProxyView):
    upstream = 'https://nms.comtactglobal.com'
    rewrite = (
        (r'/$', r'/proxy/$'),
    )

class zscalerproxyview(ProxyView):
    upstream = 'https://admin.zscalertwo.net'

