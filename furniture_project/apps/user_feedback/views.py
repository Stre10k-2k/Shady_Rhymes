import random
from django.views.generic import FormView, CreateView, ListView
from apps.core.models import Product
from .models import Order, Feedback, Cart, CartItem
from django import forms
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError

def get_or_create_cart():
    cart, _ =Cart.objects.get_or_create()
    return cart

def add_to_cart(user, obj: Product, quantity: int = 1) -> Order:
    if obj.is_active != True:
        raise ValidationError("The product isn't aviablew to buy")
    
    cart = get_or_create_cart()
    obj, created = CartItem.objects.get_or_create(cart=cart, obj=obj)

    if created:
        obj.quantity = max(1, int(quantity))
    else:
        obj.quantity = obj.quantity + max(1, int(quantity))

    obj.save(update_fields=["quantity"])
    return obj

class CartView(ListView):
    template_name = "user/cart.html"
    context_object_name = "item"
    paginate_by = 5
    model = CartItem

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "phone", "adress", "message"]

class OrderView(CreateView):
    template_name = "user/order_form.html"
    form_class = OrderCreateForm
    success_url = "user:order"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("user:order")
    
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "role", "message", "rating"]

class CommentView(CreateView):
    template_name = "user/comment.html"
    form_class = AddCommentForm
    success_url = "user:comment.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("user:comment.html")