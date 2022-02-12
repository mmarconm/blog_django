from django.contrib import admin

# Register your models here.
from articles.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published_at')
    list_filter = ('author',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'