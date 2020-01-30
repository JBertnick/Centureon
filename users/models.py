from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid

from .managers import CustomUserManager

class Licensing_modules(models.Model):
    class Meta:
        verbose_name_plural = "Licensing Modules"
    
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    created_by = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name + ":" + self.value


class Client(models.Model):
    class Meta:
        verbose_name_plural = "Clients"
    name = models.CharField(max_length=50)


    # Company Details
    company_domain = models.CharField(max_length=50, blank=True)
    vat_number = models.CharField(max_length=50, blank=True)
    company_account_num = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    head_office = models.ForeignKey('netscan.sites', on_delete=models.PROTECT, null=True, related_name='head_office')

    # Company Tech Details

    alienvault_url = models.CharField(max_length=100, blank=True)
    kibana_url = models.CharField(max_length=100, blank=True)
    zscaler_url = models.CharField(max_length=100, blank=True)
    sentielone_url = models.CharField(max_length=100, blank=True)
    solarwinds_url = models.CharField(max_length=100, blank=True)


    # Licensing
    licensed_users = models.IntegerField(default=1)
    licensed_modules = models.ManyToManyField('Licensing_modules')

    # Comtact Details
    account_manager = models.ForeignKey('CustomUser', on_delete=models.PROTECT, null=True, related_name='account_manage')
    technical_lead = models.ForeignKey('CustomUser', on_delete=models.PROTECT, null=True, related_name='account_lead')

    
    def __str__(self):
        return self.name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name_plural = "Users"
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    is_client = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)
    is_sales = models.BooleanField(default=False)
    is_demo = models.BooleanField(default=False)
    is_comtactadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_api = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True, verbose_name='last login')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def name(self):
        return self.first_name + " " + self.last_name
    
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)