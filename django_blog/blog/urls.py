from django.urls import path
from . import views

urlpatterns = [
    # Blog home (keep your existing view)
    path('', views.post_list, name='post_list'),

    # Auth routes
    path('login/', views.BlogLoginView.as_view(), name='login'),
    path('logout/', views.BlogLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]
