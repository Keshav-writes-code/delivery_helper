from django.http import HttpResponse, JsonResponse
from .models import customer_order, location, Profile
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def get_customer_locations(request):
    # show locations which customer will add
    id = 1
    customer_locations = location.objects.filter(owner_id=id).values()
    if not customer_locations:
        return HttpResponse("currently you have not added any location")
    return JsonResponse(list(customer_locations), safe=False)


@csrf_exempt
def delete_customer_locations(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            owner_id = 1
            if not isinstance(data, list):
                return JsonResponse(
                    {"error": "Expected a list of locations"}, status=400
                )
            locations = data
            if not owner_id or not locations:
                return JsonResponse(
                    {"error": "Missing owner_id or locations"}, status=400
                )

            deleted_count, _ = location.objects.filter(
                owner_id=owner_id, location_name__in=locations
            ).delete()

            if deleted_count == 0:
                return JsonResponse(
                    {"message": "No matching locations found."}, status=404
                )
            else:
                return JsonResponse(
                    {"message": f"{deleted_count} locations deleted successfully."}
                )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)


@csrf_exempt
def add_or_modify_location(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed."}, status=405)

    try:
        body = request.body.decode("utf-8")
        print("Request Body:", body)
        data = json.loads(body)
        if not isinstance(data, list):
            return JsonResponse(
                {"error": "Expected a list of location objects."}, status=400
            )

        owner_id = 2
        try:
            owner = Profile.objects.get(id=owner_id)
        except Profile.DoesNotExist:
            return JsonResponse(
                {"error": "Invalid owner_id or profile not found."}, status=404
            )

        created = []
        updated = []
        not_able_to_update = []

        for new_loc in data:
            print("Processing:", new_loc)
            required_keys = {"location_name", "longitude", "latitude"}
            if not required_keys.issubset(new_loc):
                return JsonResponse(
                    {"error": f"Missing keys in: {new_loc}"}, status=400
                )

            existing = location.objects.filter(
                owner_id=owner, location_name=new_loc["location_name"]
            ).first()

            orders_not_delivered = (
                customer_order.objects.filter(
                    customer_id=owner,
                    order_location=new_loc["location_name"],
                    is_delivered=False,
                )
                .values()
                .first()
            )
            print(orders_not_delivered)
            if existing and not orders_not_delivered:
                existing.longitude = new_loc["longitude"]
                existing.latitude = new_loc["latitude"]
                existing.save()
                updated.append(existing.location_name)

            elif not existing:
                location.objects.create(
                    owner_id=owner,
                    location_name=new_loc["location_name"],
                    longitude=new_loc["longitude"],
                    latitude=new_loc["latitude"],
                )
                created.append(new_loc["location_name"])
            else:
                not_able_to_update.append(new_loc["location_name"])

        return JsonResponse(
            {
                "message": "Processed successfully.",
                "created": created,
                "updated": updated,
                "can't_update": f"order corresponding to {not_able_to_update} is pending",
            },
            status=200,
        )

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format."}, status=400)
    except Exception as e:
        import traceback

        traceback.print_exc()
        return JsonResponse({"error": f"Something went wrong: {str(e)}"}, status=500)


def get_delivery_agent_orders(request):
    id = 2  

    orders = customer_order.objects.filter(
        assigned_delivery_agent_id=id
    ).values(
        'order_id',
        'order_name',
        'price',
        'is_delivered',
        'date_of_order',
        'date_of_delivery',
        'customer_id',
        'assigned_delivery_agent_id',
        'order_location__id',
        'order_location__location_name',
        'order_location__latitude',
        'order_location__longitude',
        'order_location__owner_id',
    )

    order_list = list(orders)

    if not order_list:
        return HttpResponse("no orders")

    return JsonResponse(order_list, safe=False)

