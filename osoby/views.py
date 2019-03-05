from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>witaj w django!</h1>")
def test(request):
    return HttpResponse("<h1>sprawdzian z matmy jutro</h1>")