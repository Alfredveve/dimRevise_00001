from django.contrib import admin
from .models import Articles



class AdminArticle(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'actif', 'slug', 'image']


admin.site.register(Articles, AdminArticle)
