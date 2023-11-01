from django.contrib import admin
from .models import DataBase


class DataBaseAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    ordering = ("first_name", )
    readonly_fields = ("first_name", "last_name", "email", "occupation")


admin.site.register(DataBase, DataBaseAdmin)
