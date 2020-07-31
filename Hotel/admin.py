from django.contrib import admin

# Register your models here.
from Hotel.models import Category, Hotel, Images

class ProductImageInline(admin.TabularInline):
    model= Images
    extra=5

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['title', 'status']
    list_filter = ['status']

class HotelAdmin(admin.ModelAdmin):
    list_display = ['title','category','gunluk_fiyat','oda_sayisi','bulundugu_il','bulundugu_ilce','status']
    list_filter = ['category']
    inlines=[ProductImageInline]
    readonly_fields = ('image_tag',)

class ImagesAdmin(admin.ModelAdmin):
    list_display= ['title', 'hotel', 'image']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Images,ImagesAdmin)
