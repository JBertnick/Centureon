from django import forms
from netscan.models import assets_master,  assets_hosts, assets_users, sites
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class assets_master_form(forms.ModelForm):
    class Meta:
        model = assets_master
        fields = ('name', 'state', 'client', 'owner', 'enabled')


class assets_hosts_form(forms.ModelForm):
    class Meta:
        model = assets_hosts
        fields = ('name', 'ip_address', 'fqdn', 'site', 'external_asset', 'operating_system', 'description', 'device_type', 'ports_open', 'tag', 'enabled', 'client')

    def __init__(self, *args, **kwargs):
        client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Device'))
        self.fields['site'].queryset = sites.objects.filter(client=client)
        self.fields['client'].initial = client

class assets_user_form(forms.ModelForm):
    class Meta:
        model = assets_users
        fields = ('first_name', 'last_name', 'username', 'email', 'site', 'role', 'manager', 'client', 'tag', 'enabled')

    def __init__(self, *args, **kwargs):
        client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save User'))
        self.fields['site'].queryset = sites.objects.filter(client=client)