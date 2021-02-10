from django.contrib import admin
from articles.models import Article
from django.contrib.auth.admin import UserAdmin
from .models import User
import logging
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    exclude = ('author',)


    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def has_view_permission(self, request, obj=None):
        if request.user.is_staff:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif obj != None: 
                if request.user == obj.author:
                    return True
        else:
            return False
        if obj is None:
            return False


    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif obj != None: 
                if request.user == obj.author:
                    return True
        else:
            return False
        if obj is None:
            return False
  

admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)