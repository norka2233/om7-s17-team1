from django.shortcuts import render
from django.views import View
from django.views import generic
from book.form import CreateBookForm, UpdateBookForm
from django.shortcuts import get_object_or_404

from .models import Book


class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        book_name = request.GET.get('book_name')
        author_surname = request.GET.get('author_surname')

        if book_name:
            books = books.filter(name__contains=book_name)

        if author_surname:
            books = books.filter(authors__surname__contains=author_surname)

        return render(request, 'book/book_list.html', context={'books': books})


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        authors = book.authors.all()
        return render(request, 'book/book_detail.html', context={'book': book, 'authors': authors})


class BookByAuthorView(View):
    def get(self, request, author_id):
        all_books = Book.objects.all()
        all_books = [b for b in all_books if author_id in [a.id for a in b.authors.all()]]
        return render(request, 'book/book_list.html', context={'books': all_books})


class BookUnorderedListView(View):
    def get(self, request):
        books = Book.objects.filter(order=None)
        return render(request, 'book/book_unordered_list.html', context={'books': books})


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


class CreateBookView(generic.CreateView):

    model = Book
    form_class = CreateBookForm
    template_name = 'book/create_update_book.html'
    success_url = '/books/book_list'
    extra_context = {'title': 'Create Book'}


class UpdateBookView(generic.UpdateView):

    model = Book
    form_class = UpdateBookForm
    template_name = 'book/create_update_book.html'
    success_url = '/books/book_list/'
    extra_context = {'title': 'Update User'}