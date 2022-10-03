# ADDED: A basic index view

from django.http import HttpResponse


def index(request):
    return HttpResponse(
        """<h2>Hello, Django. 🦄</h2>"""
    )
