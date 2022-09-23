from django.shortcuts import HttpResponse

def index(request):
    #added a request to get the name of the user, or 
    # add world and assign the result to name.
    name = request.GET.get("name") #or "world"
    return HttpResponse(f"Hello, {name}!")
