from django.contrib import admin
from .models import Watch


class WatchAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'content_object', 'created')


admin.site.register(Watch, WatchAdmin)
