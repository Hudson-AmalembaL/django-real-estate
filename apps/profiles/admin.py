from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "pkid", "user", "gender", "phone_number", "country", "city"]
    list_filter = ["gender", "country", "city"]
    list_editable_links = ["id", "pkid", "user"]
