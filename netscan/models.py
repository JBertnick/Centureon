from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class assets_tags(models.Model):
    class Meta:
        verbose_name_plural = "Assets Tags"

    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    client = models.ForeignKey('users.Client', on_delete=models.CASCADE)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name + ":" + self.value

class assets_owners(models.Model):
    class Meta:
        verbose_name_plural = "Assets Owner"

    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    client = models.ForeignKey('users.Client', on_delete=models.CASCADE, blank=True, null=True)

    tag = models.ManyToManyField(assets_tags)
    
    valid_until = models.DateField(auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    enabled = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.first_name + " " + self.second_name

class assets_master(models.Model):
    class Meta:
        verbose_name_plural = "Assets"

    name = models.CharField(max_length=50)

    STATE = (
    (1, ('Production')),
    (2, ('Development')),
    (3, ('Test')),
    (4, ('Decomissioned')),
    )

    state = models.PositiveSmallIntegerField(
    choices=STATE,
    default=1,
    )
    
    client = models.ForeignKey('users.Client', on_delete=models.CASCADE, blank=True, null=True)
    owner = models.ForeignKey(assets_owners, on_delete=models.SET_NULL, blank=True, null=True)

    limit = models.Q(app_label='netscan', model='assets_hosts') | \
        models.Q(app_label='netscan', model='assets_clouds')| \
        models.Q(app_label='netscan', model='assets_datastores')| \
        models.Q(app_label='netscan', model='assets_users')| \
        models.Q(app_label='netscan', model='assets_networks')| \
        models.Q(app_label='netscan', model='assets_virtualappliance')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, limit_choices_to=limit, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    valid_until = models.DateField(auto_now_add=False, blank=True, null=True)
    
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    enabled = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.name

class sites(models.Model):
    class Meta:
        verbose_name_plural = "Sites"

    client = models.ForeignKey('users.Client', on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=20, blank=True)
    first_line_address = models.CharField(max_length=50, blank=True)
    second_line_address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)

    is_headoffice = models.BooleanField(default=False)

    valid_until = models.DateField(auto_now_add=False, blank=True, null=True)
    
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200, blank=True)
    enabled = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.name

class assets_virtualappliance(models.Model):
    class Meta:
        verbose_name_plural = "Assets Virtual Appliance"
    
    ip_address = models.GenericIPAddressField(max_length=15)
    dns_name = models.CharField(max_length=50)

    tag = models.ManyToManyField(assets_tags, blank=True)

class assets_networks(models.Model):
    class Meta:
        verbose_name_plural = "Assets Network"
    
    name = models.CharField(max_length=50)
    cidr = models.CharField(max_length=50)
    owner = models.ForeignKey(assets_owners, blank=True, on_delete=models.PROTECT, null=True)
    description = models.CharField(max_length=250)
    
    virtual_appliance = models.ForeignKey(assets_virtualappliance, on_delete=models.CASCADE)
    external_asset = models.BooleanField(blank=True)

    client = models.ForeignKey('users.Client', on_delete=models.SET_NULL, blank=True, null=True)

    tag = models.ManyToManyField(assets_tags, blank=True)
    
    valid_until = models.DateField(auto_now_add=False, blank=True, null=True)

    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    enabled = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.cidr

class assets_hosts(models.Model):
    class Meta:
        verbose_name_plural = "Assets Host"

    name = models.CharField(max_length=50)
    ip_address = models.GenericIPAddressField(max_length=15)
    fqdn = models.CharField(max_length=50)
    site = models.ForeignKey(sites, on_delete=models.SET_NULL, blank=True, null=True)

    external_asset = models.BooleanField(blank=True)
    operating_system = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    device_type = models.CharField(max_length=250)
    ports_open = models.CharField(max_length=250, blank=True)

    client = models.ForeignKey('users.Client', on_delete=models.SET_NULL, blank=True, null=True)

    tag = models.ManyToManyField(assets_tags, blank=True)

    valid_until = models.DateField(auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    enabled = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.fqdn

class assets_users(models.Model):
    class Meta:
        verbose_name_plural = "Assets User"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    site = models.ForeignKey(sites, on_delete=models.SET_NULL, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True)
    manager = models.CharField(max_length=50, blank=True)

    client = models.ForeignKey('users.Client', on_delete=models.SET_NULL, blank=True, null=True)

    tag = models.ManyToManyField(assets_tags, blank=True)

    valid_until = models.DateField(auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    enabled = models.BooleanField(blank=False, default=True)

    @property
    def name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.name

class assets_datastores(models.Model):
    class Meta:
        verbose_name_plural = "Assets Datastores"
    
    name = models.CharField(max_length=50)
    asset_type = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    connection_string = models.CharField(max_length=250)

    tag = models.ManyToManyField(assets_tags, blank=True)

    client = models.ForeignKey('users.Client', on_delete=models.SET_NULL, blank=True, null=True)

    valid_until = models.DateField(auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    enabled = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.name

class assets_clouds(models.Model):
    class Meta:
        verbose_name_plural = "Assets Cloud"
    
    name = models.CharField(max_length=50)
    asset_type = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    PROVIDER = (
    (1, ('Azure')),
    (2, ('AWS')),
    (3, ('Softlayer')),
    (4, ('AliBaba')),
    )

    provider = models.PositiveSmallIntegerField(
      choices=PROVIDER,
      default=1,
    )

    connection_string = models.CharField(max_length=250)

    tag = models.ManyToManyField(assets_tags, blank=True)

    client = models.ForeignKey('users.Client', on_delete=models.SET_NULL, blank=True, null=True)

    valid_until = models.DateField(auto_now_add=False, blank=True, null=True)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    enabled = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.name


class assets_ports(models.Model):
    class Meta:
        verbose_name_plural = "Assets Ports"

    TYPE = (
    (1, ('tcp')),
    (2, ('udp')),
    )

    type = models.PositiveSmallIntegerField(
      choices=TYPE,
      default=1,
    )

    number = models.IntegerField()
    description = models.TextField(max_length=500)