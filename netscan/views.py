from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from netscan.forms import assets_hosts_form, assets_master_form
from django.contrib import messages

# Create your views here.

@login_required
@transaction.atomic
def update_assets_host(request):
    if request.method == 'POST':
        assetmasterform = assets_master_form(request.POST, instance=1)
        assethostform = assets_hosts_form(request.POST, instance=1)
        if assetmasterform.is_valid() and assethostform.is_valid():
            assetmasterform.save()
            assethostform.save()
            messages.success(request, ('Your asset was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        assetmasterform = assets_master_form(instance=1)
        assethostform = assets_hosts_form(instance=1)
    return render(request, 'assets-host.html', {
        'assetmasterform': assetmasterform,
        'assethostform': assethostform
    })

def new_assets_host(request):
    return render(request, 'assets-host.html', {
        'assetmasterform': assets_master_form,
        'assethostform': assets_hosts_form
    })