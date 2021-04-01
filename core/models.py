from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
LABEL_CHOICES = (
    ('NEW', 'new'),
    ('SALE', 'sale'),
    ('GIFT', 'gift')
)
class ParentCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title',unique_with='title',editable=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title= models.CharField(max_length=100)
    parent_cat= models.ForeignKey(ParentCategory,on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title',unique_with='title',editable=True)

    def __str__(self):  
        return self.title


class product(models.Model):

    title = models.CharField(max_length=100)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    description= models.TextField(max_length=500,blank=True, null=True)
    label_sale = models.CharField(choices=LABEL_CHOICES, max_length=4,blank=True,null=True)
    label_new = models.CharField(choices=LABEL_CHOICES, max_length=4,blank=True,null=True)
    label_gift = models.CharField(choices=LABEL_CHOICES, max_length=4,blank=True,null=True)
    price = models.FloatField()
    slug = AutoSlugField(populate_from='title',unique_with='title',editable=True)

    
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    created_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered= models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
