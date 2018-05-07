from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    content = render(request, "content.html", {})
    context = {
        'title': "Home Page",
        'main_content': content
    }
    return render(request, "home_page.html", context)

def form_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Home Page",
        "content": "This is content.",
        "form": contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     print(request.POST.get("fullname"))

    return render(request, "form_page.html", context)