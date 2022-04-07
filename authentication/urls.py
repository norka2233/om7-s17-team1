from django.urls import path

from authentication.views import CreateUserView, UpdateUserView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name="create_user"),
    path('update/<int:pk>/', UpdateUserView.as_view(), name="update_user"),
]