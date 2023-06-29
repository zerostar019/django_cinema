from django.contrib import admin
from .models import Film

class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Film, FilmAdmin)


