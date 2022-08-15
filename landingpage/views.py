from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'landingpage/templates/index.html', {'hello': 'Hello World!'})