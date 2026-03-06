from django.urls import path
from .views import(
    HomeView,
    ProductView,
    ProductDetailView
)

urlpatterns =[
    path("", HomeView.as_view(), name='home'),
    path("products/", ProductView.as_view(), name="product"),
    path("product/<slugify:slugify>", ProductDetailView.as_view(), name="product_detail")
]