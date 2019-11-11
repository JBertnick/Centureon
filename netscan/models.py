from django.db import models

class Enginer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

class Client_networks(models.Model):
    class Meta:
        verbose_name_plural = "Client Networks"

    network = models.CharField(max_length=15)
    client = models.ForeignKey('users.Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.network

class Agent(models.Model):
    ip_address = models.GenericIPAddressField(max_length=15)
    dns_name = models.CharField(max_length=50)
    client = models.ForeignKey('users.Client', on_delete=models.CASCADE)

class Device(models.Model):
    ip_address = models.GenericIPAddressField(max_length=15)
    dns_name = models.CharField(max_length=50)
    client = models.ForeignKey('users.Client', on_delete=models.CASCADE)
    scan_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_address
 
class Scan_data(models.Model):
    class Meta:
        verbose_name_plural = "Device Scanned Data"

    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    port = models.IntegerField(default=0)

    def __str__(self):
        return self.port