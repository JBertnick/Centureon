from django.db import models

#Create your models here.

class product_version(models.Model):
    class Meta:
        verbose_name_plural = "Product Details"

    ## Platform Notes
    
    major = models.IntegerField()
    minor = models.IntegerField()
    build = models.IntegerField()
    revision = models.IntegerField()

    is_current = models.BooleanField(default=False)

    def __str__(self):
        return str(self.major) + '.' + str(self.minor) + '.' + str(self.build) + '.' + str(self.revision)

class product_release_notes(models.Model):
    class Meta:
        verbose_name_plural = "Product Release Notes"

    version = models.ForeignKey(product_version, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self):
        return self.name + " " + str(self.version)
    

    
    
   