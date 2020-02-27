from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import BlogPost

# get -> implies that there is only 1 object
# filter -> implies that there is a [] of objects


def blog_post_list_view(request):
    # list out objects
    # could also be a search view
    qs = BlogPost.objects.all() # queryset thats a list of python objects
    template_name = "blog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # create objects, but how? use a form!

    template_name = "blog/create.html"
    context = {"form": None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # retrieve 1 object or the detail view.

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/update.html"
    context = {"object": obj, "form": None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    context = {"object": obj}
    return render(request, template_name, context)


# def blog_post_detail_page(request, slug):    
    # one way of handling errors such as /blog/400 or /blog/abc if post_id was a string in urls
    # try:
    #     obj = BlogPost.objects.get(id=post_id) # query goes into database and gives data then django renders
    # except BlogPost.DoesNotExist:
    #     raise Http404
    # except ValueError:
    #     raise Http404

    # queryset = BlogPost.objects.filter(slug=slug)
    # if queryset.count() == 0:
    #     raise Http404
    # obj = queryset.first()  # you can do queryset.last() or queryset[0]

    # obj = get_object_or_404(BlogPost, slug=slug)
    # template_name = "blog_post_detail.html"
    # context = {"object": obj}
    # return render(request, template_name, context)