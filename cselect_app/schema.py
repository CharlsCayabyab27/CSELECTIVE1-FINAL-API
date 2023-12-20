import graphene
from graphene_django import DjangoObjectType
from .models import NewUser, Status, Product, Cart, Order, OrderDetail, CartItem

class NewUserType(DjangoObjectType):
    class Meta:
        model = NewUser
        fields = "__all__"

class StatusType(DjangoObjectType):
    class Meta:
        model = Status
        fields = "__all__"

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"

class CartType(DjangoObjectType):
    class Meta:
        model = Cart
        fields = "__all__"

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = "__all__"

class OrderDetailType(DjangoObjectType):
    class Meta:
        model = OrderDetail
        fields = "__all__"

class CartItemType(DjangoObjectType):
    class Meta:
        model = CartItem
        fields = "__all__"

class Query(graphene.ObjectType):
    all_users = graphene.List(NewUserType)
    all_statuses = graphene.List(StatusType)
    all_products = graphene.List(ProductType)
    all_carts = graphene.List(CartType)
    all_orders = graphene.List(OrderType)
    all_order_details = graphene.List(OrderDetailType)
    all_cart_items = graphene.List(CartItemType)

    # Define resolve methods for each query
    def resolve_all_users(self, info, **kwargs):
        return NewUser.objects.all()

    def resolve_all_statuses(self, info, **kwargs):
        return Status.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_all_carts(self, info, **kwargs):
        return Cart.objects.all()

    def resolve_all_orders(self, info, **kwargs):
        return Order.objects.all()

    def resolve_all_order_details(self, info, **kwargs):
        return OrderDetail.objects.all()

    def resolve_all_cart_items(self, info, **kwargs):
        return CartItem.objects.all()

schema = graphene.Schema(query=Query)
