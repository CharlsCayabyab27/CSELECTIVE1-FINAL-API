from rest_framework import serializers
from .models import NewUser, Order, CartItem, Product, Status

class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'email', 'username', 'phone', 'first_name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'status_name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_code', 'product_name', 'description', 'category', 'price', 'quantity', 'attachments']

class OrderSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    user = NewUserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_date', 'status', 'total_amount']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']
