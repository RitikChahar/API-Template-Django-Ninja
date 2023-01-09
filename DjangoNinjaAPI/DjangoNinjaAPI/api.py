from django.http import JsonResponse
from ninja import NinjaAPI
import json

api = NinjaAPI()
@api.post("/fullname/")
def post_operation(request):
    request_data=json.loads(request.body)
    name=request_data['name']
    lastname=request_data['lastname']
    return JsonResponse({"Answer": f"Your name is {name} {lastname}"})