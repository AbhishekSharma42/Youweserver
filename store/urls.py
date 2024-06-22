from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('products/',ProductViewSet.as_view(),name="product-list"),
    path('products/<int:pk>/',ProductViewSet.as_view(),name="product-detail"),
    path('products/<str:pk>/',ProductViewSet.as_view(),name="product-detail-title"),

    # catagoryes
    path('category/',CategoryViewSet.as_view(),name="catagory-List"),
    path('category/<str:pk>/',CategoryViewSet.as_view(),name="catagory-detail"),

    # Simpal Home Page data 
    path('homepage/', Homepage.as_view(), name="Home-data"),

    # this path for the user create's 
    path('register/', RegisterView.as_view(), name='register'),

    # Authantication tokens genrate and use 
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

    #Get user Data After login
    path('userData/', userData.as_view(), name = "userData"),

    # Get User Cart Item's After User Login
    path('usercart/',CartSItems.as_view(), name = "userCart")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)