from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import NewUser, Order, CartItem

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['email', 'username', 'phone', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        
class CustomAuthenticationForm(AuthenticationForm):
    pass

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity'] 
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("Quantity should be at least 1.")
        return quantity
    
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})