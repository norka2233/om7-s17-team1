from django.shortcuts import render
from django.views import View

from .models import Order


class OrderList(View):
    def get(self, request):
        orders = Order.objects.order_by('created_at', 'plated_end_at').all()
        return render(request, 'order/order_list.html', context={'orders': orders})