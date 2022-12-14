from django.shortcuts import render
from django.template import context, loader
from django.http import HttpResponse
import requests

# Create your views here.
def categories(request):
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    # return HttpResponse(res.json())
    # return render(request, 'as_exercise_day4/templates/index.html')
    # return render(request, 'landingpage/templates/index.html', {'users': res})

    context = {
        'res': res
    }

    template = loader.get_template('categories.html')
    return HttpResponse(template.render(context))