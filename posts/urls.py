from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static


from .views import (
    dummy_view,
    post_list_view,
    PostView,
    EntryView,
    EntryDetailView,
    new_blog_view,
    BlogListView
)

app_name = 'posts'

urlpatterns = [
    path('', EntryView.as_view(), name='entry-list'),
    path('create/', new_blog_view, name='create-blog'),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('<int:id>/', dummy_view, name='entry-detail'),
    path('<int:id>/delete', dummy_view, name='entry-delete'),
    path('<int:id>/update', dummy_view, name='entry-update')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
