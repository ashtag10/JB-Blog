from django.urls import path 

from . import views

urlpatterns = [
    path('comments/create', views.comment_create_view, name='comment-create'),
    path('', views.home_view, name='home'),
    path('posts/<int:pk>/', views.post_detail_view, name='post-detail'),
    path('posts/post_create/', views.create_post_view, name='post-create'),
    path('posts/<int:pk>/post_update/', views.update_post_view, name= 'post-update'),
    path('posts/<int:pk>/post_delete/', views.delete_post_view, name= 'post-delete'),
    
]