from django import forms
from book.models import Book


class CreateBookForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:

        model = Book
        fields = ('name', 'description', 'count', 'authors')


class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'authors')
