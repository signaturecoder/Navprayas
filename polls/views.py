from django.http import HttpResponse

def index(request):
    return HttpResponse("hello ,World")

# Create your views here.
