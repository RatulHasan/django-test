from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    content = render(request, "content.html", {})
    context = {
        'title': "Home Page",
        'main_content': content
    }
    return render(request, "home_page.html", context)