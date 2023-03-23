from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(response):
    return render(response, 'homepage.html')