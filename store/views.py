from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import *
from .models import *


# Create your views here.
# ***************************************************************
class CategoryViewSet(APIView):
    def get(self, request, pk = None):
        if pk:
            try:
                product_catagry = Category.objects.get(name = pk);
                Catagryserializer = CategorySerializer(product_catagry);
                return Response(Catagryserializer.data);
            except Exception:
                return Response({'error': 'Product not Found'}, status = status.HTTP_404_NOT_FOUND);
        else:
            queryset = Category.objects.all();
            serializer = CategorySerializer(queryset, many=True);
        return Response(serializer.data);
# ****************************************************************


# fatch products method 
# ****************************************************************
class ProductViewSet(APIView):
    def get(self, request, pk = None):
        if pk:
            try:
                single_products = Product.objects.get(pk = pk);
                ProductSerializers = ProductSerializer(single_products);
                return Response(ProductSerializers.data);
            except Exception:
                return Response({'error': 'Product not Found'}, status = status.HTTP_404_NOT_FOUND);
        elif pk:
            try:
                single_products_by_Name = Product.objects.filter(Title = pk);
                ProductSerializersByName = ProductSerializer(single_products_by_Name);
                return Response(ProductSerializersByName.data);
            except Exception:
                return Response({'error': 'Product not Found'}, status = status.HTTP_404_NOT_FOUND);
        else:
            allProduct = Product.objects.all();
            serializer = ProductSerializer(allProduct, many=True);
        return Response(serializer.data);
# ****************************************************************      
        

# Home page View Handle
# ****************************************************************
class Homepage(APIView):
    def get(self, request):
        try:
            queryset = HomePage.objects.all();
            HomeData = HomePageSerializer(queryset, many = True);
            return Response(HomeData.data);
        except Exception:
            return Response({'error': 'Internal ser ver problem'}, status = status.HTTP_404_NOT_FOUND);
# ****************************************************************


# ****************************************************************
# User Register 
# ****************************************************************
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


# ****************************************************************
#User Address show on User Api [ user Login  required ]
# ****************************************************************
class userData(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = self.request.user;
        try:
            queryset = UserAddress.objects.filter(userId=user)
            userdata = UserAddreSerializer(queryset, many = True)
            return Response(userdata.data)
        except Exception:
            pass
        return Response({"server error":"internal server error"})
        

# ****************************************************************
# User Cart's Item Show on User API [ user Login  required ]
# ****************************************************************
class CartSItems(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = self.request.user;

        queryset = CartITems.objects.filter(userId = user)
        userCartItems = CartITemsSerializer(queryset, many = True);
        # print(userCartItems.data);
        return Response(userCartItems.data)


     