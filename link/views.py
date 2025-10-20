from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import TelegramLink, Category, LinkLike, Comment
from .forms import TelegramLinkForm, CommentForm


def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            # Log the user in
            user = authenticate(username=username, password=password)
            login(request, user)
            
            messages.success(request, f'Welcome {username}! Your account has been created.')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})


def home(request):
    """Home page with all links"""
    links = TelegramLink.objects.filter(is_active=True).select_related('user')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        links = links.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Filter by category (now using string values instead of ID)
    category = request.GET.get('category')
    if category:
        links = links.filter(category=category)
    
    # Filter by type
    link_type = request.GET.get('type')
    if link_type:
        links = links.filter(link_type=link_type)
    
    # Sort options
    sort_by = request.GET.get('sort', 'recent')
    if sort_by == 'popular':
        links = links.order_by('-views_count', '-created_at')
    elif sort_by == 'liked':
        links = links.order_by('-likes_count', '-created_at')
    else:  # recent
        links = links.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(links, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': TelegramLink.CATEGORY_CHOICES,  # Use choices from model
        'search_query': search_query,
        'selected_category': category,  # Now stores string value
        'selected_type': link_type,
        'sort_by': sort_by,
        'link_types': TelegramLink.LINK_TYPES,
    }
    
    return render(request, 'links/home.html', context)

@login_required
def upload_link(request):
    """Upload a new Telegram link"""
    if request.method == 'POST':
        form = TelegramLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            messages.success(request, 'Your Telegram link has been uploaded successfully!')
            return redirect('link_detail', hash_id=link.hash_id)
    else:
        form = TelegramLinkForm()
    
    return render(request, 'links/upload_link.html', {'form': form})

def link_detail(request, hash_id):
    """View details of a specific link"""
    link = get_object_or_404(TelegramLink, hash_id=hash_id, is_active=True)
    
    # Increment view count
    link.increment_views()
    
    # Check if user has liked this link
    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = LinkLike.objects.filter(user=request.user, link=link).exists()
    
    # Get comments
    comments = link.comments.select_related('user').filter(is_active=True)
    
    # Comment form
    comment_form = CommentForm()
    
    # Related links
    related_links = TelegramLink.objects.filter(
        category=link.category,
        is_active=True
    ).exclude(hash_id=link.hash_id)[:4]  # Changed from pk to hash_id
    
    context = {
        'link': link,
        'user_has_liked': user_has_liked,
        'comments': comments,
        'comment_form': comment_form,
        'related_links': related_links,
    }
    
    return render(request, 'links/link_detail.html', context)

@login_required
def edit_link(request, hash_id):
    """Edit an existing link"""
    link = get_object_or_404(TelegramLink, hash_id=hash_id, user=request.user)
    
    if request.method == 'POST':
        form = TelegramLinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Link updated successfully!')
            return redirect('link_detail', hash_id=link.hash_id)
    else:
        form = TelegramLinkForm(instance=link)
    
    return render(request, 'links/edit_link.html', {'form': form, 'link': link})

@login_required
def delete_link(request, hash_id):
    """Delete a link"""
    link = get_object_or_404(TelegramLink, hash_id=hash_id, user=request.user)
    
    if request.method == 'POST':
        link.is_active = False
        link.save()
        messages.success(request, 'Link deleted successfully!')
        return redirect('my_links')
    
    return render(request, 'links/delete_link.html', {'link': link})

@login_required
def my_links(request):
    """View user's own links"""
    links = TelegramLink.objects.filter(user=request.user, is_active=True).order_by('-created_at')
    
    paginator = Paginator(links, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'links/my_links.html', {'page_obj': page_obj})

@login_required
def toggle_like(request, hash_id):
    """Toggle like on a link (AJAX)"""
    if request.method == 'POST':
        link = get_object_or_404(TelegramLink, hash_id=hash_id)
        like, created = LinkLike.objects.get_or_create(user=request.user, link=link)
        
        if not created:
            like.delete()
            link.likes_count -= 1
            liked = False
        else:
            link.likes_count += 1
            liked = True
        
        link.save(update_fields=['likes_count'])
        
        return JsonResponse({
            'success': True,
            'liked': liked,
            'likes_count': link.likes_count
        })
    
    return JsonResponse({'success': False}, status=400)

@login_required
def add_comment(request, hash_id):
    """Add a comment to a link"""
    if request.method == 'POST':
        link = get_object_or_404(TelegramLink, hash_id=hash_id)
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.link = link
            comment.save()
            messages.success(request, 'Comment added successfully!')
        else:
            messages.error(request, 'Error adding comment.')
    
    return redirect('link_detail', hash_id=hash_id)


@login_required
def delete_comment(request, pk):  # Use pk for comments
    """Soft delete comment by setting is_active=False"""
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    comment.is_active = False
    comment.save()
    messages.success(request, 'Comment deleted successfully!')
    return redirect('link_detail', hash_id=comment.link.hash_id)  # Use hash_id for the link

def category_links(request, category_id):
    """View links by category"""
    category = get_object_or_404(Category, pk=category_id)
    links = TelegramLink.objects.filter(category=category, is_active=True).order_by('-created_at')
    
    paginator = Paginator(links, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'links/category_links.html', {
        'category': category,
        'page_obj': page_obj
    })