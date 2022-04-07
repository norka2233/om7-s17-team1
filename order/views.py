from django.shortcuts import render
from django.views import View
from django.db.models import F
from order.forms import CreateOrderForm, UpdateOrderForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Order
from authentication.models import CustomUser
import pytz


class OrderList(View):
    def get(self, request):
        orders = Order.objects.order_by('created_at', 'plated_end_at').all()
        return render(request, 'order/order_list.html', context={'orders': orders})


class FilteredOrderList(View):
    def get(self, request):
        orders = Order.objects \
            .filter(plated_end_at__gte=F('end_at')) \
            .order_by('created_at', 'plated_end_at') \
            .all()
        return render(request, 'order/order_list.html', context={'orders': orders})


class CreateOrderView(generic.CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = 'order/order_create.html'
    success_url = reverse_lazy('order_list')


class UpdateOrderView(generic.UpdateView):
    model = Order
    form_class = UpdateOrderForm
    template_name = 'order/order_update.html'
    success_url = reverse_lazy('order_list')
