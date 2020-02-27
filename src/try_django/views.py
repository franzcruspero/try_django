from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPost

def home_page(request):
    context = {"content": "Home Page"}
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Welcome to Try Django", "blog_list": qs}
    return render(request, "home.html", context)

def about_page(request):
    context = {"content": "About Us"}
    return render(request, "about.html", context)

def contact_page(request):
    # print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact Us", 
        "form": form,
    }
    return render(request, "form.html", context)

def example_page(request):
    context = {"content": "Example"}
    template_name = "hello_world.html"
    template_object = get_template(template_name)
    rendered_item = template_object.render(context)
    return HttpResponse(rendered_item)
