from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import customer_order
# Create your views here.
def get_delivery_location(request):
    return


def get_customer_locations(request):
    return


def delete_customer_locations(request):
    return


def add_or_modify_location(request):
    return

def show_orders(request):
    id=4
    orders=customer_order.objects.filter(assigned_delivery_agent_id=id).values()
    order_list=list(orders)
    print(order_list)
    if not order_list:
        return HttpResponse("no orders")

    else:
        return JsonResponse({"orders":order_list})

        
