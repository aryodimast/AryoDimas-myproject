from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    return res.json()
    return render(request, 'landingpage/templates/index.html', {'users': res})