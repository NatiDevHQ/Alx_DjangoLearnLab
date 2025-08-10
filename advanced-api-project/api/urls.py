from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.DetailView.as_view(), name='book-detail'),
    path('books/create/', views.CreateView.as_view(), name='add-book'),
    path('books/update/<int:pk>/', views.UpdateView.as_view(), name='update-book'),
    path('books/delete/<int:pk>/', views.DeleteView.as_view(), name='delete-book'),
]
