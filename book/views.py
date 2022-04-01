import operator

from django.shortcuts import render
from django.views import View
from django.db.models import F

from django.views.generic import ListView

from .models import Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        context = {'books': books}
        return render(request, 'book/book_list.html', context=context)


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
        books = Book.objects.order_by('id')
        context = {'books': books}
        return render(request, 'book/book_list.html', context=context)




