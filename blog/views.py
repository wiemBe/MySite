from django.shortcuts import render
from django.http import HttpResponse


def startingPage(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def postDetail(request):
    return HttpResponse("detail")
 