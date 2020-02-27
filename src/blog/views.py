from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BlogPostForm, BlogPostModelForm
from .models import BlogPost

# get -> implies that there is only 1 object
# filter -> implies that there is a [] of objects


def blog_post_list_view(request):
    # list out objects
    # could also be a search view
    qs = BlogPost.objects.all().published() # queryset thats a list of python objects
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = "blog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    # create objects, but how? use a form!
    # form = BlogPostForm(request.POST or None)
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False) # -> in case you want to make changes through the view
        # obj.title = form.cleaned_data.get("title") + '0' -> adds a 0 to title
        # obj2 = AnotherModel.objects.create(title=title) -> this is assuming you had another model
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()

    template_name = "blog/form.html"
    context = {"form": form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # retrieve 1 object or the detail view.

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = "blog/form.html"
    context = {"form": form, "title":f"Update {obj.title}"}
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
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