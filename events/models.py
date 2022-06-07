from django.db import models
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse 
from helpers.to_base64 import image_as_base64

class Category(models.Model):
    subject = models.CharField(max_length=20)
    fa_class = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.subject}'

class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    author = models.CharField(max_length=50, blank=True)
    author_img = models.ImageField(upload_to='author_img/%Y/%m/%d/', blank=True)
    author_img64 = models.TextField(blank=True, null=True)
    author_title = models.CharField(max_length=100, blank=True)
    author_details = models.TextField(blank=True)
    title = models.CharField(max_length=100)
    details = models.TextField()
    details2 = models.TextField(blank=True)
    details3 = models.TextField(blank=True)
    details4 = models.TextField(blank=True)
    details5 = models.TextField(blank=True)
    details6 = models.TextField(blank=True)
    details7 = models.TextField(blank=True)
    details8 = models.TextField(blank=True)
    block_quote = models.TextField(blank=True)
    date = models.DateField()
    main_image = models.ImageField(upload_to='main_events/%Y/%m/%d/', blank=True)
    main_image64 = models.TextField(blank=True, null=True)
    sub_image = models.ImageField(upload_to='sub_image/%Y/%m/%d/', blank=True)
    sub_image2 = models.ImageField(upload_to='sub_image2/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.title}'
        
    def get_absolute_url(self):
        return reverse('events:detail', args=[self.id]) 

    def save(self, *args, **kwargs):
        if not self.main_image64:
            self.main_image64 = image_as_base64(self.main_image)
        if not self.author_img64:
            self.author_img64 = image_as_base64(self.author_img)
        super().save(*args, **kwargs)
