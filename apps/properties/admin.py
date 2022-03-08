from django.contrib import admin
from .models import Property, PropertyViews


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "property_type", "advert_type", "country"]
    list_filter = ["advert_type", "property_type"]


admin.site.register(PropertyViews)
