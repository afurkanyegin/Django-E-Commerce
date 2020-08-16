from django.contrib import admin

# Register your models here.
from Home.models import Setting, UserProfile, ContactFormMessage


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message','status']
    readonly_fields = ['name','email','subject','message','ip']
    list_filter = ['status']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','address','city','country','image_tag']

admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile,UserProfileAdmin)
