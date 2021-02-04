from django.contrib import admin
from articles.models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    pass



admin.site.register(Article, ArticleAdmin)