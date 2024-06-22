from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ColorCategory(models.Model):
    colors = models.CharField(max_length=10)
    def __str__(self):
        return self.colors


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default="",upload_to="static/Category")
    desc = models.TextField()
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    Title = models.CharField(max_length=100);
    image = models.ImageField(default="", upload_to="static/Products/")
    Desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stocks = models.PositiveIntegerField()
    size = models.CharField(max_length=5);
    color = models.CharField(max_length=20);
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    def __str__(self):
        return self.Title


class HomePage(models.Model):
    TopBanner_title = models.CharField(max_length=100)
    TopBanner_paragraph = models.TextField()
    TopBanner_image = models.ImageField(upload_to='static/HeadBanner/')
    Foote_title = models.CharField(max_length=50)
    Footer_text = models.TextField(max_length=255)
    Footer_Contact_num = models.CharField(max_length=12)
    Footer_Contact_mail = models.CharField(max_length=50)
    def __str__(self):
        return self.TopBanner_title;


class UserAddress(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.address_line1}, {self.city}"


class CartITems(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE);
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE);
    Quantity = models.DecimalField(max_digits=10, decimal_places=2)



