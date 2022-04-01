from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_list/book_list_asc', views.BookListOrderedAsc.as_view(), name='book_list/book_list_asc'),
    path('book_list/book_list_desc', views.BookListOrderedDesc.as_view(), name='book_list/book_list_desc'),
    path('book_list/book_list_count', views.BookListOrderedCount.as_view(), name='book_list/book_list_count'),

]
