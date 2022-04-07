from django.urls import path
from author.views import AuthorListView, AuthorDetailView, create_author, edit_author

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name="author_list"),
    path('<int:pk>/', AuthorDetailView.as_view(), name="author_detail"),
    path('create_author/', create_author, name="create_author"),
    path('<int:pk>/edit_author/', edit_author, name="edit_author"),
]