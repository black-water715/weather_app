from django.shortcuts import render


def author(request):
    template="author.html"
    return render(request, template)


def info(request):
    template="info.html"
    return render(request, template)
