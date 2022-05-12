from django.urls import path, re_path

from .views import dummy_view, post_list_view


app_name = 'posts'
urlpatterns = [
    path('', post_list_view, name='entry-list'),
    path('<int:id>/', dummy_view, name='entry-detail'),
    path('<int:id>/delete', dummy_view, name='entry-delete'),
    path('<int:id>/update', dummy_view, name='entry-update')
]