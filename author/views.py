from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from author.models import Author
from .forms import CreateAuthorForm


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = "authors"
    template_name = 'author/author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = "author"
    template_name = 'author/author_detail.html'


def create_author(request):
    if request.method == "POST":
        form = CreateAuthorForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('author_detail', pk=post.pk)
    else:
        form = CreateAuthorForm

    return render(request, 'author/create_author.html', {'form': form})


def edit_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = CreateAuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = CreateAuthorForm(instance=author)
    return render(request, 'author/edit_author.html', {'form': form, 'pk': pk})