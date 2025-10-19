from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_telegram_url(value):
    """Validate that the URL is a Telegram link"""
    if not (value.startswith('https://t.me/') or value.startswith('http://t.me/')):
        raise ValidationError('Please enter a valid Telegram link (t.me)')

class Category(models.Model):

    
    """Categories for organizing Telegram links"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class TelegramLink(models.Model):
    """Model for storing Telegram links"""
    LINK_TYPES = [
        ('channel', 'Channel'),
        ('group', 'Group'),
        
    ]
    CATEGORY_CHOICES = [
    # Technology & Programming
    ('tech', 'Technology'),
    ('programming', 'Programming'),
    ('web_dev', 'Web Development'),
    ('mobile_dev', 'Mobile Development'),
    ('ai_ml', 'AI & Machine Learning'),
    ('cybersecurity', 'Cybersecurity'),
    ('blockchain', 'Blockchain & Crypto'),
    
    # Business & Finance
    ('business', 'Business'),
    ('entrepreneurship', 'Entrepreneurship'),
    ('marketing', 'Marketing'),
    ('finance', 'Finance & Investing'),
    ('crypto_trading', 'Crypto Trading'),
    
    # Education & Learning
    ('education', 'Education'),
    ('language', 'Language Learning'),
    ('programming_courses', 'Programming Courses'),
    
    # Entertainment
    ('entertainment', 'Entertainment'),
    ('gaming', 'Gaming'),
    ('movies_tv', 'Movies & TV Shows'),
    ('music', 'Music'),
    ('anime', 'Anime & Manga'),
    
    # Social & Community
    ('social', 'Social'),
    ('dating', 'Dating'),
    ('local', 'Local Communities'),
    
    # News & Media
    ('news', 'News'),
    ('politics', 'Politics'),
    ('tech_news', 'Tech News'),
    
    # Health & Wellness
    ('health', 'Health & Wellness'),
    ('fitness', 'Fitness'),
    ('mental_health', 'Mental Health'),
    
    # Hobbies & Interests
    ('travel', 'Travel'),
    ('food', 'Food & Cooking'),
    ('sports', 'Sports'),
    ('fashion', 'Fashion'),
    
    # Regional
    ('india', 'India'),
    ('usa', 'USA'),
    ('europe', 'Europe'),
    
    # Miscellaneous
    ('other', 'Other'),
]

    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='telegram_links')
    title = models.CharField(max_length=200, help_text="Title or name of the Telegram link")
    url = models.URLField(max_length=500, validators=[validate_telegram_url])
    description = models.TextField(blank=True, help_text="Brief description of the link")
    link_type = models.CharField(max_length=20, choices=LINK_TYPES, default='other')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    
    # Metadata
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False, help_text="Verified by admin")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['link_type']),
            models.Index(fields=['is_active']),
        ]
    
    def __str__(self):
        return self.title
    
    def increment_views(self):
        """Increment view count"""
        self.views_count += 1
        self.save(update_fields=['views_count'])

class LinkLike(models.Model):
    """Track user likes on links"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(TelegramLink, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'link')
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} likes {self.link.title}"

class Comment(models.Model):
    """Comments on Telegram links"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.ForeignKey(TelegramLink, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.link.title}"