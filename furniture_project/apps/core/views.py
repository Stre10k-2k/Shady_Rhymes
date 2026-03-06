import random
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = Product.objects.filter(
            Q(is_activate__icontaims = True)
        )

        ids = list(qs.values_list("id", flat=True)[:200])
        random_ids = random.sample(ids, min(len(ids), 4)) if ids else []
        random_obj = list(
            Product.objects.filter(ids__in=random_ids)
        )

        random_obj.sort(key=lambda x: random_ids.index(x.id))

        ctx["random_obj"] = random_obj

        return ctx

class ProductViews(ListView):
    template_name = 'core/products.html'
    context_object_name = 'product'
    paginate_by = 12

class ProductDetailView(DetailView):
    template_name = 'core/detail.html'
    model = Product
    slug_field = "slugify"
    slug_url_kwarg = "slugify"