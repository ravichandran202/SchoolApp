from django.shortcuts import render

# Create your views here.
def signin(requests):
    return render(requests,"signin.html")