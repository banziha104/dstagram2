from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','author','created','updated')
    list_filter = ('author','created','updated')
    search_fields = ('text','created')
    raw_id_fields = ('author',)
    ordering = ['updated','created']

admin.site.register(Photo, PhotoAdmin)