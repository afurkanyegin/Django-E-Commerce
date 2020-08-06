from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import TextField
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    STATUS=(('True','Evet'),('False','Hayır'),)
    parent =TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    title=models.CharField(blank=True,max_length=150)
    keywords=models.CharField(blank=True,max_length=255)
    description=models.CharField(blank=True,max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by=['title']

    def __str__(self):
        full_path = [self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return ' -> '.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Hotel(models.Model):
    STATUS=(('True','Evet'),('False','Hayır'),)
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    keywords=models.CharField(blank=True,max_length=255)
    description=models.CharField(blank=True,max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    bulundugu_il=models.CharField(blank=True,max_length=255)
    bulundugu_ilce=models.CharField(blank=True,max_length=255)
    gunluk_fiyat=models.FloatField()
    oda_sayisi=models.IntegerField()
    detail=RichTextUploadingField()
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Images(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image=models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

