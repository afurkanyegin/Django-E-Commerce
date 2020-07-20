from django.contrib import admin

# Register your models here.
from Hotel.models import Category, Hotel


class CategoryAdmin(admin.ModelAdmin):
    list_display= ['title', 'status']
    list_filter = ['status']

class HotelAdmin(admin.ModelAdmin):
    list_display = ['title','category','status','bosoda']
    list_filter = ['category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Hotel,HotelAdmin)
