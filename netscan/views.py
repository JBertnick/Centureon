from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponseForbidden
from netscan.models import assets_clouds, assets_datastores, assets_hosts, assets_master, assets_networks, assets_owners, assets_users, sites
from netscan.forms import assets_hosts_form, assets_user_form, sites_form, assets_datastores_form, assets_networks_form, assets_clouds_form
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta, date
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import json


# Master View

@login_required(login_url='/login/')
def assetsview(request):
    if request.user.is_authenticated:
        client = request.user.client
        assets = assets_master.objects.filter(client=client)
    else:
        client = ''
        pass

    today = date.today()
    start_date = '2020-01-01'

    day7 = assets_master.objects.filter(client=client, created_at__range=[start_date, today]).count()
    day6 = assets_master.objects.filter(client=client, created_at__range=[start_date, today + timedelta(days=-1)]).count()
    day5 = assets_master.objects.filter(client=client, created_at__range=[start_date, today + timedelta(days=-2)]).count()
    day4 = assets_master.objects.filter(client=client, created_at__range=[start_date, today + timedelta(days=-3)]).count()
    day3 = assets_master.objects.filter(client=client, created_at__range=[start_date, today + timedelta(days=-4)]).count()
    day2 = assets_master.objects.filter(client=client, created_at__range=[start_date, today + timedelta(days=-5)]).count()
    day1 = assets_master.objects.filter(client=client, created_at__range=[start_date, today + timedelta(days=-6)]).count()

    days = {
        'day1': day1,
        'day2': day2,
        'day3': day3,
        'day4': day4,
        'day5': day5,
        'day6': day6,
        'day7': day7
    }

    args = {'client': client, 'assets': assets, 'days': days}
    return render(request, 'assets.html', args)

# User Views

@login_required(login_url='/login/')
def usersview(request):
    if request.user.is_authenticated:
        client = request.user.client
        users = assets_users.objects.filter(client=client)
    else:
        client = ''
        users = ''
        pass
    args = {'users': users}
    return render(request, 'users.html', args)

@login_required(login_url='/login/')
def userdetailedview(request, id):
    client = request.user.client
    try:
        user  = assets_users.objects.get(client=client, id=id)
        if request.method == "POST":
            if request.POST.get("delete", "yes"):
                user.delete()
            else:
                pass
    except ObjectDoesNotExist:
        return redirect(assetsview)
        
    # Need to add error page if you try to hack us! - Ensure that Client is verfied as being the owner
    args = {'client': client, 'user': user}
    return render(request, 'user-display.html', args)

@login_required(login_url='/login/')
def useraddview(request, id=None):
    form = assets_user_form(client=request.user.client)
    if id:
        client = request.user.client
        try:
            user = assets_users.objects.get(client=client, id=id)
            form = assets_user_form(client=request.user.client, instance=user)
        except assets_users.DoesNotExist:
            return redirect('/home/assets/users')
    if request.method == "POST":
        if id:
            form = assets_user_form(request.POST, client=request.user.client, instance=user)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/users/' + str(id) )
            else:
                print(form.errors)
        else:
            form = assets_user_form(request.POST, client=request.user.client)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/users')
            else:
                print(form.errors)
    args = {'form': form}
    return render(request, 'user-form.html', args)

# Site Views

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
def sitedetailedview(request, id):
    client = request.user.client
    try:
        site  = sites.objects.get(client=client, id=id)
        if request.method == "POST":
            if request.POST.get("delete", "yes"):
                site.delete()
            else:
                pass
    except ObjectDoesNotExist:
        return redirect(assetsview)

    # Need to add error page if you try to hack us! - Ensure that Client is verfied as being the owner
    args = {'client': client, 'site': site}
    return render(request, 'site-display.html', args)

@login_required(login_url='/login/')
def siteaddview(request, id=None):
    form = sites_form(client=request.user.client)
    if id:
        client = request.user.client
        try:
            site = sites.objects.get(client=client, id=id)
            form = sites_form(client=request.user.client, instance=site)
        except sites.DoesNotExist:
            return redirect('/home/assets/sites')
    if request.method == "POST":
        if id:
            form = sites_form(request.POST, client=request.user.client, instance=site)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/sites/' + str(id) )
            else:
                print(form.errors)
        else:
            form = sites_form(request.POST, client=request.user.client)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/sites')
            else:
                print(form.errors)
    print(form)
    args = {'form': form}
    return render(request, 'site-form.html', args)

# Device Views

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
def devicesdetailedview(request, id):
    client = request.user.client
    try:
        device  = assets_hosts.objects.get(client=client, id=id)
        if request.method == "POST":
            if request.POST.get("delete", "yes"):
                device.delete()
            else:
                pass
    except ObjectDoesNotExist:
        return redirect(assetsview)
        
    # Need to add error page if you try to hack us! - Ensure that Client is verfied as being the owner
    args = {'client': client, 'device': device}
    return render(request, 'device-display.html', args)

@login_required(login_url='/login/')
def deviceaddview(request, id=None):
    form = assets_hosts_form(client=request.user.client)
    if id:
        client = request.user.client
        try:
            device = assets_hosts.objects.get(client=client, id=id)
            form = assets_hosts_form(client=request.user.client, instance=device)
        except assets_hosts.DoesNotExist:
            return redirect('/home/assets/devices')
    if request.method == "POST":
        if id:
            form = assets_hosts_form(request.POST, client=request.user.client, instance=device)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/devices/' + str(id) )
            else:
                print(form.errors)
        else:
            form = assets_hosts_form(request.POST, client=request.user.client)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/devices')
            else:
                print(form.errors)

    args = {'form': form}
    return render(request, 'device-form.html', args)

# Datastore Views

@login_required(login_url='/login/')
def datastoresview(request):
    if request.user.is_authenticated:
        client = request.user.client
        datastores = assets_datastores.objects.filter(client=client)
    else:
        client = ''
        pass
    args = {'datastores': datastores}
    return render(request, 'datastores.html', args)

@login_required(login_url='/login/')
def datastoredetailedview(request, id):
    client = request.user.client
    try:
        datastore  = assets_datastores.objects.get(client=client, id=id)
        if request.method == "POST":
            if request.POST.get("delete", "yes"):
                datastore.delete()
            else:
                pass
    except ObjectDoesNotExist:
        return redirect(assetsview)
        
    # Need to add error page if you try to hack us! - Ensure that Client is verfied as being the owner
    args = {'client': client, 'datastore': datastore}
    return render(request, 'datastore-display.html', args)

@login_required(login_url='/login/')
def datastoreaddview(request, id=None):
    form = assets_datastores_form(client=request.user.client)
    if id:
        client = request.user.client
        try:
            datastore = assets_datastores.objects.get(client=client, id=id)
            form = assets_datastores_form(client=request.user.client, instance=datastore)
        except assets_datastores.DoesNotExist:
            return redirect('/home/assets/datastores')
    if request.method == "POST":
        if id:
            form = assets_datastores_form(request.POST, client=request.user.client, instance=datastore)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/datastores/' + str(id) )
            else:
                print(form.errors)
        else:
            form = assets_datastores_form(request.POST, client=request.user.client)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/datastores')
            else:
                print(form.errors)
    args = {'form': form}
    return render(request, 'datastore-form.html', args)

# Cloud Views

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
def clouddetailedview(request, id):
    client = request.user.client
    try:
        cloud  = assets_clouds.objects.get(client=client, id=id)
        if request.method == "POST":
            if request.POST.get("delete", "yes"):
                cloud.delete()
            else:
                pass
    except ObjectDoesNotExist:
        return redirect(assetsview)
        
    # Need to add error page if you try to hack us! - Ensure that Client is verfied as being the owner
    args = {'client': client, 'cloud': cloud}
    return render(request, 'cloud-display.html', args)

@login_required(login_url='/login/')
def cloudaddview(request, id=None):
    form = assets_clouds_form(client=request.user.client)
    if id:
        client = request.user.client
        try:
            cloud = assets_clouds.objects.get(client=client, id=id)
            form = assets_clouds_form(client=request.user.client, instance=cloud)
        except assets_clouds.DoesNotExist:
            return redirect('/home/assets/clouds')
    if request.method == "POST":
        if id:
            form = assets_clouds_form(request.POST, client=request.user.client, instance=cloud)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/clouds/' + str(id) )
            else:
                print(form.errors)
        else:
            form = assets_clouds_form(request.POST, client=request.user.client)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/clouds')
            else:
                print(form.errors)
    args = {'form': form}
    return render(request, 'cloud-form.html', args)

# Network Views

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
def networkdetailedview(request, id):
    client = request.user.client
    try:
        network  = assets_networks.objects.get(client=client, id=id)
        if request.method == "POST":
            if request.POST.get("delete", "yes"):
                network.delete()
            else:
                pass
    except ObjectDoesNotExist:
        return redirect(assetsview)
        
    # Need to add error page if you try to hack us! - Ensure that Client is verfied as being the owner
    args = {'client': client, 'network': network}
    return render(request, 'network-display.html', args)

@login_required(login_url='/login/')
def networkaddview(request, id=None):
    form = assets_networks_form(client=request.user.client)
    if id:
        client = request.user.client
        try:
            network = assets_networks.objects.get(client=client, id=id)
            form = assets_networks_form(client=request.user.client, instance=network)
        except assets_networks.DoesNotExist:
            return redirect('/home/assets/networks')
    if request.method == "POST":
        if id:
            form = assets_networks_form(request.POST, client=request.user.client, instance=network)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/networks/' + str(id) )
            else:
                print(form.errors)
        else:
            form = assets_networks_form(request.POST, client=request.user.client)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.client = request.user.client
                obj.save()
                return redirect('/home/assets/networks')
            else:
                print(form.errors)
    args = {'form': form}
    return render(request, 'network-form.html', args)

# Add Tags Views

#@login_required(login_url='/login/')
#def tagsaddview(request):
#    form = assets_tag_form(client=request.user.client)
#    if request.method == "POST":
#        form = assets_tag_form(request.POST, client=request.user.client)
#        if form.is_valid():
#            obj = form.save(commit=False)
#            obj.client = request.user.client
#            obj.save()
#            return redirect('/home/assets/tag')
#    args = {'form': form}
#    return render(request, 'tags-form.html', args)