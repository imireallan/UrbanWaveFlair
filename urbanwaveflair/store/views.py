from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from urbanwaveflair.store.models import Collection, Product
from urbanwaveflair.store.serializers import CollectionSerializer, ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.orderitems.count() > 0:
            return Response(
                {
                    "error": "This product cannot be deleted because it includes one or more order items"
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count("products"))
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        collection = self.get_object()
        if collection.products.count() > 0:
            return Response(
                {
                    "error": "This collection cannot be deleted because it includes on or more product."
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)
