from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]
    
    list_display = ["title", "body", "author"]
    


class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "author", "comment"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
