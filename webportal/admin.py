from django.contrib import admin
from .models import product_release_notes, product_version

admin.site.register(product_release_notes)
admin.site.register(product_version)

