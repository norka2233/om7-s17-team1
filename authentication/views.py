from django.views import generic

from authentication.forms import CreateUserForm, UpdateUserForm
from authentication.models import CustomUser


class CreateUserView(generic.CreateView):

    model = CustomUser
    form_class = CreateUserForm
    template_name = 'authentication/create_update_user.html'
    success_url = '/books/book_list'
    extra_context = {'title': 'Create User'}


class UpdateUserView(generic.UpdateView):

    model = CustomUser
    form_class = UpdateUserForm
    template_name = 'authentication/create_update_user.html'
    success_url = '/books/book_list/'
    extra_context = {'title': 'Update User'}