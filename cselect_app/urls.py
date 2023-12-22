from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views
from rest_framework.routers import DefaultRouter
from .schema import schema
from graphene_django.views import GraphQLView
from django.contrib.auth import views as auth_views





from .views import (
    NewUserViewSet,
    StatusViewSet,
    ProductViewSet,
    OrderViewSet,
    CartItemViewSet,
)
router = DefaultRouter()
router.register(r'users', NewUserViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', views.home_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('get_cart_data/', views.get_cart_data, name='get_cart_data'),
    path('api/users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('api/statuses/<int:pk>/', views.StatusDetailView.as_view(), name='status-detail'),
    path('api/products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('api/orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('api/cart-items/<int:pk>/', views.CartItemDetailView.as_view(), name='cartitem-detail'),
    path('api/products/', views.ProductListView.as_view(), name='product-list'),
    path('api/orders/', views.OrderListView.as_view(), name='order-list'),
    path('api/users/', views.NewUserListView.as_view(), name='NewUser-list'),
    path('api/cart-items/', views.CartItemListView.as_view(), name='CartItem-list'),
    
    path('api/cart-items/update/<int:pk>/', views.CartItemUpdateView.as_view(), name='CartItem-list-Update'),
    path('api/cart-items/delete/<int:pk>/', views.CartItemDeleteView.as_view(), name='CartItem-list-Delete'),

    path('api/products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='Product-Update'),
    path('api/products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='Product-Delete'),
    
    path('api/orders/update/<int:pk>/', views.OrderUpdateView.as_view(), name='Orders-Update'),
    path('api/orders/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='Orders-Delete'),
    
    path('api/users/update/<int:pk>/', views.UserUpdateView.as_view(), name='NewUser-Update'),
    path('api/users/delete/<int:pk>/', views.UserDeleteView.as_view(), name='NewUser-Delete'),
    
    path('api/users/create/', views.UserCreateView.as_view(), name='NewUser-Create'),
    
    path('api/product/create/', views.ProductCreateView.as_view(), name='NewUser-Create'),
    path('api/order/create/', views.OrderCreateView.as_view(), name='NewUser-Create'),
    
    path('api/checkout/', views.CheckoutView.as_view(), name='NewUser-Create'),
    
    path('api/users/update-delete/<int:pk>', views.UserUpdateDeleteView.as_view(), name='User-UpdateDelete'),
    
    path('api/products/update-delete/<int:pk>', views.ProductUpdateDeleteView.as_view(), name='Product-UpdateDelete'),
    
    path('api/orders/update-delete/<int:pk>', views.OrderUpdateDeleteView.as_view(), name='Order-UpdateDelete'),
    
    

    
    
    
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    
]