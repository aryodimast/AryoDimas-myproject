from django.shortcuts import render
import requests

# Create your views here.
def categories(request):
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    print(res.json())
    return render(request, 'as_exercise_day4/templates/index.html', {'res': res})
    # return render(request, 'landingpage/templates/index.html', {'users': res})