from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    #added a request to get the name of the user, or 
    # add world and assign the result to name.
    name = request.Get("name") or "world"
    return HttpResponse("Hello, {}!".format(name))
