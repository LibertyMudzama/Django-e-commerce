from django.db import models
from django.conf import settings

LABEL_CHOICES = (
    ('NEW', 'new'),
    ('SALE', 'sale'),
    ('GIFT', 'gift')
)

class Category(models.Model):
    title= models.CharField(max_length=100)

    def __str__(self):  
        return self.title


class product(models.Model):

    title = models.CharField(max_length=100)
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    label_sale = models.CharField(choices=LABEL_CHOICES, max_length=4,blank=True)
    label_new = models.CharField(choices=LABEL_CHOICES, max_length=4,blank=True)
    label_gift = models.CharField(choices=LABEL_CHOICES, max_length=4,blank=True)
    price = models.FloatField()

    
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
