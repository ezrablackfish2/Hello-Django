from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse("Hello, World and ezra \n how are you\n!")
