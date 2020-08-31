from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product, Category


class ProductDetailView(DetailView):
    Model = Product
    context_object_name = "product"

    template_name = "shop/products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductListView(ListView):
    model = Product
    context_object_name = "products"

    template_name = "shop/products/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Product.category
        return context


def show_category(request, hierarchy=None):
    category_slug = hierarchy.split("/")
    parent = None
    root = Category.objects.all()

    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug=slug)

    try:
        instance = Category.objects.get(parent=parent, slug=category_slug[-1])
    except:
        instance = get_object_or_404(Product, slug=category_slug[-1])
        return render(
            request, "shop/products/product_detail.html", {"instance": instance}
        )
    else:
        return render(request, "shop/products/categories.html", {"instance": instance})

