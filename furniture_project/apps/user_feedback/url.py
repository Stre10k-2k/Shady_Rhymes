from django.urls import path
from .views import(
    CartView,
    OrderView,
    CommentView
)

urlpatterns = [
    path("cart/", CartView.as_view, name="cart"),
    path("order/", OrderView.as_view(), name="order"),
    path("comment/", CommentView.as_view(), name="comment")
]