from django.shortcuts import render, redirect
from users.models import Client, CustomUser
from netscan.models import sites, assets_master, assets_networks, assets_users, assets_hosts, assets_clouds, assets_datastores, assets_virtualappliance
from .models import product_version, product_release_notes
from django.contrib.auth import login, authenticate
from users.forms import CompanyAddUserForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

def rootview(request):
    response = redirect('/home/')
    return response

def homeview(request):
    
    version = product_version.objects.filter(is_current=True).first()
    notes = product_release_notes.objects.filter(version=version).first()
    
    if request.user.is_authenticated:
        client = request.user.client
    else:
        client = ''
        pass

    args = {'client': client, 'version': version, 'product_notes': notes}
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
    else:
        client = ''
        pass
    args = {'client': client}
    return render(request, 'company.html', args)

@login_required(login_url='/login/')
def companyvaview(request):
    if request.user.is_authenticated:
        client = request.user.client
        va = assets_virtualappliance.objects.filter(client=client)
    else:
        client = ''
        pass
    args = {'client': client, 'va': va}
    return render(request, 'company-va.html', args)

@login_required(login_url='/login/')
def companyvadetails(request, id):
    client = request.user.client
    try:
        va = assets_virtualappliance.objects.get(client=client, id=id)
        if request.method == "POST":
            if request.POST.get("delete", "yes"):
                va.delete()
            else:
                pass
    except ObjectDoesNotExist:
        return redirect(companyvaview)

    args = {'client': client, 'va': va}
    return render(request, 'company-va-display.html', args)

@login_required(login_url='/login/')
def usersview(request):
    if request.user.is_authenticated:
        client = request.user.client
        users_unfiltered = CustomUser.objects.filter(client=client)
        users = users_unfiltered.exclude(is_api=True)
    else:
        client = ''
        pass
    args = {'client': client, 'users': users}
    return render(request, 'company-users.html', args)

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


