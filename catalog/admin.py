from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

"""
# Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""
admin.site.register(Genre)
admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    pass
