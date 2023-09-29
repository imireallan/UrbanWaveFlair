from django.urls import path

from urbanwaveflair.store import views

urlpatterns = [
    path("products/", views.products_list),
    path("products/<int:id>", views.product_detail),
    path("collections/", views.collections_list),
    path("collections/<int:pk>", views.collection_detail, name="collection-detail"),
]
