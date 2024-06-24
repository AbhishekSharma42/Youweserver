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
from decouple import config

# ***************************************************************
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
# User Register [ Login not required ]
# ****************************************************************
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
# ****************************************************************


# ****************************************************************
#User Address show on User Api [ user Login  required ]
# ****************************************************************
class UserData(generics.ListAPIView):
    
    # User Authantications By Default
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    # User Address get if user [added]
    def get(self, request):
        user = self.request.user;

        try:
            queryset = UserAddress.objects.filter(userId = user)
            userdata = UserAddreSerializer(queryset, many = True)
            return Response(userdata.data)
        except Exception:
            return Response({"server error":"Some error acurde"})
        return Response({"server error":"internal server error"})


    # User Address Register if user Not Add own [address]
    def post(self, request):
         user = self.request.user
         data = request.data.copy()
         data['userId'] = user.id

         serializer = UserAddreSerializer(data = data)
         if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # User Address Update by user if User Add own [Address] 
    def put(self, request):
        user = self.request.user
        data = request.data.copy()
        data['userId'] = user.id
        
        try:
            address = UserAddress.objects.get(pk = 1, userId = user)
        except UserAddress.DoesNotExist:
            return Response({"error": "Address not found or does not belong to the user"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserAddreSerializer(address, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
# ****************************************************************


# ****************************************************************
# User Cart's Item Show on User API [ user Login  required ]
# ****************************************************************
class CartSItems(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    # get to the all cartItems login required
    def get(self, request):
        user = self.request.user;

        queryset = CartITems.objects.filter(userId = user).select_related('product_id', 'userId')
        userCartItems = CartITemsSerializer(queryset, many = True);
        return Response(userCartItems.data);

    # Delete cart's item login required
    def delete(self, request, pk = None):
        user = request.user
        try:
            cart_item = CartITems.objects.get(pk=pk, userId=user)
            cart_item.delete()
            return Response({"Success": "Cart item deleted"}, status=status.HTTP_204_NO_CONTENT)
        except CartITems.DoesNotExist:
            return Response({"Error": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

# ****************************************************************


# ****************************************************************
# User OrderItem Item Show on User API [ user Login  required ]
# ****************************************************************
class OrderItem(generics.ListAPIView):
    permission_classes = [IsAuthenticated];
    serializer_class = UserSerializer;

    def get(self, request):
        user = self.request.user;
        try:
            queryset = OrderItems.objects.filter(userId = user);
            userdata = OrderItemsSerializer(queryset, many = True);
            return Response(userdata.data);
        except Exception:
            return Response({"server error":"Some error acurde"});
        return Response({"server error":"internal server error"});
# ******************************************************************
