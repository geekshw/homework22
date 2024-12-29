from django.contrib import admin
from .models import Banner

class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')

admin.site.register(Banner, BannerAdmin)
