from django.contrib import admin

from gallery.models import ImageClass, TagClass


admin.site.register(ImageClass)
admin.site.register(TagClass)
