from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import customer_order,location
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def get_delivery_location(request):
    return


def get_customer_locations(request):
    # show locations which customer will add 
    id = 1
    customer_locations = location.objects.filter(owner_id=id).values()
    if not customer_locations:
        return HttpResponse("currently you have not added any location")
    return JsonResponse(list(customer_locations),safe=False)


@csrf_exempt
def delete_customer_locations(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            owner_id = 1
            locations = data.get("locations", [])

            if not owner_id or not locations:
                return JsonResponse({"error": "Missing owner_id or locations"}, status=400)

            deleted_count, _ = location.objects.filter(owner_id=owner_id, location_name__in=locations).delete()

            if deleted_count == 0:
                return JsonResponse({"message": "No matching locations found."}, status=404)
            else:
                return JsonResponse({"message": f"{deleted_count} locations deleted successfully."})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method is allowed"},status=405)

def add_or_modify_location(request):
    return

def show_orders(request):
    id=4
    orders=customer_order.objects.filter(assigned_delivery_agent_id=id).values()
    order_list=list(orders)
    if not order_list:
        return HttpResponse("no orders")

    else:
        return JsonResponse(order_list,safe=False)

        
