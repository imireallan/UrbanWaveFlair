from typing import Any
from urllib.parse import urlencode

from django.contrib import admin
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.urls import reverse
from django.utils.html import format_html

from urbanwaveflair.store.models import Collection, Customer, Order, OrderItem, Product


class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [("<10", "Low")]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "products_count"]
    search_fields = ["title"]

    @admin.display(ordering="products_count")
    def products_count(self, collection):
        url = (
            reverse("admin:store_product_changelist")
            + "?"
            + urlencode({"collection__id": collection.id})
        )
        return format_html(
            "<a href={} target='_blank'>{}</a>", url, collection.products_count
        )

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(products_count=Count("product"))


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership", "orders"]
    list_editable = ["membership"]
    list_per_page = 10
    search_fields = ["first_name__istartswith", "last_name__istartswith"]

    def orders(self, customer):

        url = (
            reverse("admin:store_order_changelist")
            + "?"
            + urlencode({"customer__id": customer.id})
        )
        return format_html(
            "<a href={} target='_blank'>{} Orders</a>", url, customer.orders
        )

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(orders=Count("order"))


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    autocomplete_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ["customer"]
    inlines = [OrderItemInline]
    list_display = ["id", "placed_at", "payment_status", "customer"]
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ["clear_inventory"]
    autocomplete_fields = ["collection"]
    list_display = ["title", "unit_price", "inventory_status", "collection_title"]
    list_editable = ["unit_price"]
    list_per_page = 10
    list_select_related = ["collection"]
    list_filter = ["collection", "last_update", InventoryFilter]
    prepopulated_fields = {"slug": ["title"]}
    search_fields = ["title"]

    @admin.action(description="Clear inventory")
    def clear_inventory(self, request, queryset):
        inventory_count = queryset.update(inventory=0)
        self.message_user(
            request, f"{inventory_count} products were successfully updated"
        )

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product: Product):
        if product.inventory > 10:
            return "Ok"
        return "Low"
