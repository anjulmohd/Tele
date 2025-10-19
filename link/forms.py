from django import forms
from .models import TelegramLink, Comment

class TelegramLinkForm(forms.ModelForm):
    class Meta:
        model = TelegramLink
        fields = ['title', 'url', 'description', 'link_type', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Python Developers Group'
            }),
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://t.me/yourlink'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe what this link is about...'
            }),
            'link_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'required': 'required'  # Add this
            }),
        }
        help_texts = {
            'url': 'Enter a valid Telegram link (starting with t.me)',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment...'
            }),
        }
        labels = {
            'text': 'Your Comment'
        }