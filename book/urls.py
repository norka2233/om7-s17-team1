from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:book_id>', views.BookDetailView.as_view(), name='book_detail'),
    path('book_unordered_list/', views.BookUnorderedListView.as_view(), name='book_unordered_list')
]
