from django.contrib import admin
from .models import *
from django.utils.html import format_html, mark_safe
# Register your models here.

admin.site.site_header="Youwe Fashion"
admin.site.site_brand="WELCOME TO YOUWE FASHION"
admin.site.site_title="Youwe"
admin.site.site_logo="https://img.icons8.com/?size=80&id=TCe5LffUfgZD&format=png"
admin.site.search_model:["auth.User"]


class Categorie(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_preview','desc','modified_at']

    def image_preview(self, obj):
        return mark_safe('<img src="{}" style="max-width:100px; max-height:100px" />'.format(obj.image.url))

    image_preview.allow_tags = True
    image_preview.short_description = 'Images'
admin.site.register(Category, Categorie)



class AdminProducts(admin.ModelAdmin):
    list_display = ['Title','image_preview','price','category','stocks']

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-width:80px; max-height:80px; border:2px solid white; order-radius: 50px" />'.format(obj.image.url))
        image_preview.allow_tags = True
        image_preview.short_description = 'Images'
admin.site.register(Product, AdminProducts)



@admin.register(UserAddress)
class UserAddress(admin.ModelAdmin):
    list_display = ['userId','address_line1', 'city','mobile']



@admin.register(CartITems)
class AdminCatrts(admin.ModelAdmin):
    list_display = ['userId','product_id','Quantity']



@admin.register(HomePage)
class HomePagedata(admin.ModelAdmin):
    list_display = ['TopBanner_title','image_preview','Footer_Contact_num','Footer_Contact_mail']
    
    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-width:80px; max-height:80px" />'.format(obj.TopBanner_image.url))
        image_preview.allow_tags = True
        image_preview.short_description = 'Images'

