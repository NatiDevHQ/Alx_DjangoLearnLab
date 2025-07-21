from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, RegisterView
from .views import register_view


urlpatterns = [
  path('books/', list_books, name='list_books'),
  path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
