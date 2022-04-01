from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Book
from .models import Author



class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book/book_list.html', context={'books': books})


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'book/book_detail.html', context={'book': book})


class BookByAuthorView(View):
    def get(self, request, author_id):
        all_books = Book.objects.all()

        all_books = [b for b in all_books if author_id in [a.id for a in b.authors.all()]]

        return render(request, 'book/book_list.html', context={'books': all_books})
