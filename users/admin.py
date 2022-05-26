from django.contrib import admin

from posts.models import Author, Blog, Entry

admin.site.register(Author)
admin.site.register(Blog)


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass
