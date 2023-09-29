from django.db.models import Count
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from urbanwaveflair.store.models import Collection, Product
from urbanwaveflair.store.serializers import CollectionSerializer, ProductSerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def delete(self, request):
        product = self.get_object()
        if product.orderitems.count() > 0:
            return Response(
                {
                    "error": "This product cannot be deleted because it includes one or more order items"
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionList(ListCreateAPIView):
    queryset = Collection.objects.annotate(products_count=Count("products"))
    serializer_class = CollectionSerializer


class CollectionDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.annotate(products_count=Count("products"))

    def delete(self, request):
        collection = self.get_object()
        if collection.products.count() > 0:
            return Response(
                {
                    "error": "This collection cannot be deleted because it includes on or more product."
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
