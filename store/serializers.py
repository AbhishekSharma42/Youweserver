from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# *********************************************************
# User Create public serializer 
# *********************************************************
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        users = User.objects.create_user(username = validated_data['username'], password = validated_data['password'])
        return users
# *********************************************************



# *********************************************************
# User Address [ protected serializer ]
# *********************************************************
class UserAddreSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='userId.username')

    class Meta:
        model = UserAddress 
        fields = ['user_name','address_line1','address_line2','city','pincode','country','mobile']
# *********************************************************



# *********************************************************
# User product [ public serializer ]
# *********************************************************
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
# *********************************************************




# *********************************************************
# User Cart items protected serializer
# *********************************************************
class CartITemsSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(source='id')
    ProductTitle = serializers.CharField(source='product_id.Title')
    productimage = serializers.CharField(source='product_id.image')
    productDesc = serializers.CharField(source='product_id.Desc')
    productprice = serializers.CharField(source='product_id.price')
    productsize = serializers.CharField(source='product_id.size')
    productcolor = serializers.CharField(source='product_id.color')
    productcategory = serializers.CharField(source='product_id.category')
    
    class Meta:
        model = CartITems
        fields = ['_id','ProductTitle','productimage','Quantity','productDesc','productprice','productsize','productcolor','productcategory']
# *********************************************************



# *********************************************************
# User Category [ public serializer ]
# *********************************************************
class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems;
        fields = '__all__'
# *********************************************************




# *********************************************************
# User Category [ public serializer ]
# *********************************************************
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
# *********************************************************



# *********************************************************
# User Homepage public serializer
# *********************************************************
class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'
# *********************************************************
