from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        users = User.objects.create_user(username = validated_data['username'], password = validated_data['password'])
        return users




class UserAddreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress 
        fields = '__all__'
        # read_only_fields = ['userId']






class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




class CartITemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartITems
        fields = "__all__"





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'







class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'


