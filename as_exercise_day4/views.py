from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests

# Create your views here.
def categories(request):
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    # return HttpResponse(res.json())

    template = loader.get_template('index.html')
    return HttpResponse(template.render())