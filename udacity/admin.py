from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Art


class ArrtAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ttttile',         {'fields': ['title']}),
        ('Art werk spot',   {'fields': ['art']}),
    ]

    list_display = ('title', 'art', 'created', 'id', 'pk', 'coords')
    list_filter = ['art']
    search_fields = ['title']

admin.site.register(Art, ArrtAdmin)