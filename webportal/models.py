from django.db import models

# Create your models here.

class product_version(models.Model):
    class Meta:
        verbose_name_plural = "Product Details"

    ## Platform Notes
    
    major = models.IntegerField()
    minor = models.IntegerField()
    build = models.IntegerField()
    revision = models.IntegerField()

    def __str__(self):
        return str(major) + str(minor) + str(build) + str(revision)

class product_release_notes(models.Model):
    class Meta:
        verbose_name_plural = "Product Release Notes"

    version = models.ForeignKey(product_version, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    notes = models.TextField()

    
    
   