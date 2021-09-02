from app.models import Games, Genres, Publishers, Tags
from django.contrib import admin

# Register your models here.

admin.site.register(Genres)
admin.site.register(Tags)
admin.site.register(Publishers)
admin.site.register(Games)
