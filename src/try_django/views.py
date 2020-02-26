from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    context = {"content": "Home Page"}
    if request.user.is_authenticated:
        context = {"content": "Home Page", "my_list": [1,2,3,4,5]}
    return render(request, "home.html", context)

def about_page(request):
    context = {"content": "About Us"}
    return render(request, "about.html", context)

def contact_page(request):
    context = {"content": "Contact Us"}
    return render(request, "contact.html", context)

def example_page(request):
    context = {"content": "Example"}
    template_name = "hello_world.html"
    template_object = get_template(template_name)
    rendered_item = template_object.render(context)
    return HttpResponse(rendered_item)
