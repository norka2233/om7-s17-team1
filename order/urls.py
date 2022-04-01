from django.urls import path
from . import views


urlpatterns = [
    path('order_list/', views.OrderList.as_view(), name='order_list'),
    path('order_whitelist/', views.FilteredOrderList.as_view(), name='order_whitelist')
]