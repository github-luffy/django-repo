from django.contrib import admin
from MyDjangoSite.books.models import Publisher, Book, Author
# Register your models here.


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')
    fields = ('name', 'address', 'city', 'state_province', 'country', 'website')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  # list_display
    search_fields = ('first_name', 'last_name')     # show quick_search_box
    fields = ('first_name', 'last_name', 'email')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('title', 'publisher', 'publication_date',)   # notice:','.show today,before 7 days,this month, this year
    date_hierarchy = 'publication_date'  # search some day content
    ordering = ('-publication_date',)  # descending order
    # fields = ('title', 'authors', 'publisher', 'publication_date',) # show items you want to change
    filter_horizontal = ('authors',) # deal with : ManyToMany
    raw_id_fields = ('publisher',) # deal with : ForeignKey

admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
