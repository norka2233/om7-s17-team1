from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:book_id>', views.BookDetailView.as_view(), name='book_detail'),
    path('book_by_author_id/<int:author_id>', views.BookByAuthorView.as_view(), name='book_by_author_id')
]
