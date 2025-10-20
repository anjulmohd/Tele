from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Main views
    path('', views.home, name='home'),
    path('upload/', views.upload_link, name='upload_link'),
    path('link/<str:hash_id>/', views.link_detail, name='link_detail'),
    path('link/<str:hash_id>/edit/', views.edit_link, name='edit_link'),
    path('link/<str:hash_id>/delete/', views.delete_link, name='delete_link'),
    path('link/<str:hash_id>/like/', views.toggle_like, name='toggle_like'),
    path('link/<str:hash_id>/comment/', views.add_comment, name='add_comment'),
    path('my-links/', views.my_links, name='my_links'),
    path('category/<int:category_id>/', views.category_links, name='category_links'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]