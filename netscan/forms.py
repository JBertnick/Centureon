from django import forms
from netscan.models import assets_master,  assets_hosts

class assets_master_form(forms.ModelForm):
    class Meta:
        model = assets_master
        fields = ('name', 'state', 'client', 'owner', 'enabled')


class assets_hosts_form(forms.ModelForm):
    class Meta:
        model = assets_hosts
        fields = ('name', 'ip_address', 'fqdn', 'site', 'external_asset', 'operating_system', 'description', 'device_type', 'ports_open',    )
