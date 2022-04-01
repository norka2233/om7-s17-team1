from django.shortcuts import render
from django.views import View

from .models import Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        book_name = request.GET.get('book_name').strip()
        author_surname = request.GET.get('author_surname').strip()

        if book_name:
            books = books.filter(name__contains=book_name)

        if author_surname:
            books = books.filter(authors__surname__contains=author_surname)

        return render(request, 'book/book_list.html', context={'books': books})


class BookListOrderedAsc(View):
    def get(self, request):
        books = Book.objects.order_by('name').all()
        return render(request, 'book/book_list.html', context={'books': books})


class BookListOrderedDesc(View):
    def get(self, request):
        books = Book.objects.order_by('-name').all()
        return render(request, 'book/book_list.html', context={'books': books})


class BookListOrderedCount(View):
    def get(self, request):
        books = Book.objects.order_by('count')
        return render(request, 'book/book_list.html', context={'books': books})


class UserBookList(View):
    def get(self, request, user_id):
        books = Book.objects.filter(order__user=user_id)
        return render(request, 'book/user_book_list.html', context={'books': books})
