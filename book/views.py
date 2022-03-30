from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book/book_list.html', context={'books': books})


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'book/book_detail.html', context={'book': book})
