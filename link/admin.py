from django.contrib import admin
from .models import TelegramLink, Category, LinkLike, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'link_count')
    search_fields = ('name', 'description')
    
    def link_count(self, obj):
        return obj.links.count()
    link_count.short_description = 'Number of Links'

@admin.register(TelegramLink)
class TelegramLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'link_type', 'category', 'views_count', 'likes_count', 'is_active', 'is_verified', 'created_at')
    list_filter = ('link_type', 'category', 'is_active', 'is_verified', 'created_at')
    search_fields = ('title', 'description', 'url', 'user__username')
    readonly_fields = ('views_count', 'likes_count', 'created_at', 'updated_at')
    list_editable = ('is_active', 'is_verified')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'title', 'url', 'description')
        }),
        ('Classification', {
            'fields': ('link_type', 'category')
        }),
        ('Status', {
            'fields': ('is_active', 'is_verified')
        }),
        ('Statistics', {
            'fields': ('views_count', 'likes_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(LinkLike)
class LinkLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'link', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'link__title')
    date_hierarchy = 'created_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'link', 'text_preview', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'link__title', 'text')
    date_hierarchy = 'created_at'
    
    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Comment Preview'