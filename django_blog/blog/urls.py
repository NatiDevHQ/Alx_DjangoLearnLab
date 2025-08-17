from django.urls import path
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.BlogLoginView.as_view(), name='login'),
    path('logout/', views.BlogLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Blog Post URLs (ALX expects singular 'post')
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    # Comment CRUD
path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_update'),
path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

]