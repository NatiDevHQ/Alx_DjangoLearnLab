from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.BlogLoginView.as_view(), name='login'),
    path('logout/', views.BlogLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]