from django.urls import path

from apps.views import ProductListTemplateView, ProductListDetailView

urlpatterns = [
    path('', ProductListTemplateView.as_view(), name='home'),
    path('product-detail', ProductListDetailView.as_view(), name='product_list'),
]