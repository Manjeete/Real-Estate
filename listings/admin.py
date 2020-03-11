from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    search_fields = ('title', 'description', 'price', 'state', 'address', 'zipcode','city')
    list_per_page = 25
    list_editable = ('is_published',)

admin.site.register(Listing, ListingAdmin)
