from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date, datetime
from django.views import View, generic

import random


from .models import Entry, Blog
from .forms import BlogModelForm


def dummy_view(request):
    now = datetime.utcnow()
    html = "<html><body><h1>%s</h1></body></html>" % now

    return HttpResponse(html)


def post_list_view(request):
    return render(request, 'posts.html', {})


# class-based view
class PostView(View):
    def get(self):
        return render(self.request, 'posts.html', {})


# Generic class-based view
class EntryView(generic.ListView):
    model = Entry
    context_object_name = 'object_list'
    template_name = 'entry_list'

    # add new variable to the current context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_integer'] = random.randint(1, 100)
        return context

    # define a new query set
    def get_queryset(self):
        # filtering
        return Entry.objects.filter(id=1)


class EntryDetailView(generic.DetailView):
    model = Entry

    def get_object(self, queryset=None):
        obj = super().get_object()
        return obj


def new_blog_view(request):
    form = BlogModelForm(request.POST or None, request.FILES or None)
    e = Blog.objects.all()
    for i in e:
        if i.image is not None:
            print('images: ', i.image)
    if form.is_valid():
        print('new blog view',
              form.cleaned_data.get('name'),
              form.cleaned_data.get('tagline'),
              form.cleaned_data.get('image')
              )
        form.save()
        return redirect('entries:blog-list')

    context = {
        'form': form,
    }

    return render(request, 'new_post.html', context)


# A CBV to get all the posts
class BlogListView(generic.ListView):
    model = Blog

