from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the estimations index.")

def project_details(request, project_id):
    return HttpResponse("You're looking at Project %s." % project_id)
