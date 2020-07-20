from django.contrib import admin

# Register your models here.
from Hotel.models import Category, Hotel


class CategoryAdmin(admin.ModelAdmin):
    list_display= ['title', 'status']
    list_filter = ['status']

class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_adi','category','gunluk_fiyat','oda_sayisi','bulundugu_il','bulundugu_ilce','status']
    list_filter = ['category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Hotel,HotelAdmin)
