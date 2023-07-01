from django.contrib import admin

# Register your models here.
from .models import VacuumCleaner


class VacuumCleanerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'picture')
    search_fields = ('name',)


admin.site.register(VacuumCleaner, VacuumCleanerAdmin)
