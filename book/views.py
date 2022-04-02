from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.db.models import F

from django.views.generic import ListView

from .models import Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book/book_list.html', context={'books': books})


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        return render(request, 'book/book_detail.html', context={'book': book})


class BookUnorderedListView(View):
    def get(self, request):
        books = Book.objects.filter(order=None)
        return render(request, 'book/book_unordered_list.html', context={'books': books})


class BookListOrderedAsc(View):
    def get(self, request):
        books = Book.objects.order_by('name').all()
        context = {'books': books}
        return render(request, 'book/book_list.html', context=context)


class BookListOrderedDesc(View):
    def get(self, request):
        books = Book.objects.order_by('-name').all()
        context = {'books': books}
        return render(request, 'book/book_list.html', context=context)


class BookListOrderedCount(View):
    def get(self, request):
        books = Book.objects.order_by('count')
        context = {'books': books}
        return render(request, 'book/book_list.html', context=context)
