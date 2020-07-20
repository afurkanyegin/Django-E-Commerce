from django.db import models

from django.db.models import TextField


class Category(models.Model):
    STATUS=(('True','Evet'),('False','Hayır'),)
    parent =models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Hotel(models.Model):
    STATUS=(('True','Evet'),('False','Hayır'),)

    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    hotel_adi=models.CharField(max_length=150)
    keywords=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    bulundugu_il=models.CharField(max_length=255)
    bulundugu_ilce=models.CharField(max_length=255)
    gunluk_fiyat=models.FloatField()
    oda_sayisi=models.IntegerField()
    #detail=RichTextUploadingField()
    detail=TextField()
    status=models.CharField(max_length=10,choices=STATUS)
    slug=models.SlugField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.hotel_adi

