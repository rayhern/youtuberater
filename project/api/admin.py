from django.contrib import admin
from .models import Video, Rating


class VideoTable(admin.ModelAdmin):
    list_display = ('id', 'url', 'title')

class RatingTable(admin.ModelAdmin):
    list_display = ('id', 'video', 'user', 'stars')


# Register your models here.
admin.site.register(Video, VideoTable)
admin.site.register(Rating, RatingTable)
