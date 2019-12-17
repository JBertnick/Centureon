from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from netscan.models import assets_clouds, assets_datastores, assets_hosts, assets_master, assets_networks, assets_owners, assets_users, sites
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@login_required(login_url='/login/')
def networksview(request):
    if request.user.is_authenticated:
        client = request.user.client
        networks = assets_networks.objects.filter(client=client)
    else:
        client = ''
        networks = ''
        pass
    args = {'client': client, 'networks': networks}
    return render(request, 'networks.html', args)

@login_required(login_url='/login/')
def sitesview(request):
    if request.user.is_authenticated:
        client = request.user.client
        cs = sites.objects.filter(client=client)
    else:
        client = ''
        cs = ''
        pass
    args = {'client': client, 'sites': cs}
    return render(request, 'sites.html', args)

@login_required(login_url='/login/')
def assetsview(request):
    if request.user.is_authenticated:
        client = request.user.client
        assets = assets_master.objects.filter(client=client)
    else:
        client = ''
        pass
    args = {'client': client, 'assets': assets}
    return render(request, 'assets.html', args)

@login_required(login_url='/login/')
def devicesview(request):
    if request.user.is_authenticated:
        client = request.user.client
        devices = assets_hosts.objects.filter(client=client)
    else:
        client = ''
        pass
    args = {'client': client, 'devices': devices}
    return render(request, 'devices.html', args)

@login_required(login_url='/login/')
def cloudsview(request):
    if request.user.is_authenticated:
        client = request.user.client
        clouds = assets_clouds.objects.filter(client=client)
    else:
        client = ''
        pass
    args = {'client': client, 'clouds': clouds}
    return render(request, 'clouds.html', args)

@login_required(login_url='/login/')
def datastoresview(request):
    if request.user.is_authenticated:
        client = request.user.client
        datastores = assets_datastores.objects.filter(client=client)
    else:
        client = ''
        pass
    args = {'client': client, 'datastores': datastores}
    return render(request, 'datastores.html', args)


@login_required(login_url='/login/')
def usersview(request):
    if request.user.is_authenticated:
        client = request.user.client
        users = assets_users.objects.filter(client=client)
    else:
        client = ''
        users = ''
        pass
    args = {'client': client, 'users': users}
    return render(request, 'users.html', args)

@login_required(login_url='/login/')
def devicesdetailedview(request, id):
    client = request.user.client
    try:
        device  = assets_hosts.objects.get(client=client, id=id)
    except ObjectDoesNotExist:
        return redirect(assetsview)
    # Need to add error page if you try to hack us! - Ensure that Client is verfied as being the owner
    args = {'client': client, 'device': device}
    return render(request, 'device-display.html', args)