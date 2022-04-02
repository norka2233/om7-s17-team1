from django.shortcuts import render
from django.views import View
from django.db.models import F
from django.shortcuts import get_object_or_404


from .models import Order


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
