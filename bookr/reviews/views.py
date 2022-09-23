from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    name = request.Get.get("name") or "world"
    return HttpResponse("Hello, world!")
