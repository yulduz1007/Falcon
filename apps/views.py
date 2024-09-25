from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ProductListTemplateView(TemplateView):
    template_name = "apps/product/product-grid.html"


class ProductListDetailView(TemplateView):
    template_name = "apps/product/product-details.html"
