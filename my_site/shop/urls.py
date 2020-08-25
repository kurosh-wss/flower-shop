from django.urls import path
from django.views.generic import TemplateView


app_name = "shop"

urlpatterns = [
    path("", TemplateView.as_view(template_name="shop/base.html")),
    path(
        "products/",
        TemplateView.as_view(template_name="shop/products/product_list.html"),
    ),
    path(
        "products/1/",
        TemplateView.as_view(template_name="shop/products/product_detail.html"),
    ),
]
