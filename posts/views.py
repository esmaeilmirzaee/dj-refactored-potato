from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from django.views import View, generic
from .models import Entry


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
class EntryDetailView(generic.ListView):
    model = Entry
    context_object_name = 'object_list'
    template_name = 'entry_list'


