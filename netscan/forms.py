from django import forms
from netscan.models import assets_master,  assets_hosts, assets_users, sites, assets_datastores, assets_clouds, assets_networks, assets_tags
from users.models import Client
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class assets_hosts_form(forms.ModelForm):
    class Meta:
        model = assets_hosts
        fields = ('name', 'ip_address', 'fqdn', 'site', 'external_asset', 'operating_system', 'description', 'device_type', 'tag', 'enabled', 'client')

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
        self.fields['client'].initial = client


class sites_form(forms.ModelForm):
    class Meta:
        model = sites
        fields = ('name', 'first_line_address', 'second_line_address', 'city', 'postal_code', 'description', 'enabled', 'client')

    def __init__(self, *args, **kwargs):
        client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Site'))
        self.fields['client'].initial = client

class assets_datastores_form(forms.ModelForm):
    class Meta:
        model = assets_datastores
        fields = ('name', 'asset_type', 'description', 'site', 'connection_string', 'external_asset', 'tag', 'enabled', 'client')

    def __init__(self, *args, **kwargs):
        client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Datastore'))
        self.fields['site'].queryset = sites.objects.filter(client=client)
        self.fields['client'].initial = client

class assets_clouds_form(forms.ModelForm):
    class Meta:
        model = assets_clouds
        fields = ('name', 'asset_type', 'description', 'site', 'provider', 'connection_string', 'external_asset', 'tag', 'enabled', 'client')

    def __init__(self, *args, **kwargs):
        client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Datastore'))
        self.fields['site'].queryset = sites.objects.filter(client=client)
        self.fields['client'].initial = client

class assets_networks_form(forms.ModelForm):
    class Meta:
        model = assets_networks
        fields = ('name', 'cidr', 'owner', 'site', 'virtual_appliance', 'description', 'external_asset', 'tag', 'enabled', 'client')

    def __init__(self, *args, **kwargs):
        client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Network'))
        self.fields['site'].queryset = sites.objects.filter(client=client)
        self.fields['client'].initial = client

class assets_tag_form(forms.ModelForm):
    class Meta:
        model = assets_tags
        fields = ('name', 'value', 'client')

    def __init__(self, *args, **kwargs):
        client = kwargs.pop('client', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Tag'))
        self.fields['client'].initial = client