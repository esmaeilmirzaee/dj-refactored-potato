from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from django.views import View


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

