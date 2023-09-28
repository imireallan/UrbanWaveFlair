from django.shortcuts import render

# from django.db.models import Q, ExpressionWrapper, F
# from django.db.models.aggregates import Min, Count, Max, Avg, Sum
# from django.db import transaction
# from urbanwaveflair.store.models import Customer, Collection, Product, Order, OrderItem


def say_hello(request):
    # customers with .com accounts
    # customers_queryset = Customer.objects.filter(email__icontains='.com')
    # list(customers_queryset)
    # collections that don't have a featured product
    # collections_queryset = Collection.objects.filter(featured_product__isnull=True)
    # list(collections_queryset)
    # products with low inventory, (less than 10)
    # products_queryset = Product.objects.filter(inventory__lt=10)
    # list(products_queryset)
    # Orders placed by customer with id = 1
    # orders_queryset = Order.objects.filter(customer__id=1)
    # list(orders_queryset)
    # orderItems for products in collection 3
    # orderItems_queryset = OrderItem.objects.filter(product__collection__id=3)
    # list(orderItems_queryset)
    # Products: inventory < 10 AND unit_price < 20
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # products that have been ordered and sort them by title
    # orderitems_queryset = OrderItem.objects.values("product_id").distinct()

    # queryset = Product.objects.filter(id__in=orderitems_queryset).order_by('title')

    # get the last 5 orders with their customer and items (incl product)
    # queryset = Order.objects.select_related('customer').order_by('-placed_at')[:5].prefetch_related('orderitem_set__product')
    # list(queryset)

    # how many orders do we have?
    # orders = Order.objects.aggregate(Count('id'))
    # orders = Order.objects.count()

    # how many units of product 1 have we sold?
    # orders = OrderItem.objects.filter(product_id=1).aggregate(units_sold=Sum('quantity'))

    # how many orders has customer 1 placed
    # orders  = Order.objects.filter(customer_id=1).aggregate(Count('id'))

    # products = Product.objects.filter(collection_id=3).aggregate(Max('unit_price'), Min('unit_price'), Avg('unit_price'))
    # print(orders)

    # customers with their last order id
    # customers_queryset = Customer.objects.annotate(last_order_id=Max('order__id'))
    # print(customers_queryset)

    # collections and count of their products
    # collections = Collection.objects.annotate(products_count=Count('product'))
    # print(collections)

    # customers with more than 5 orders
    # customers = Customer.objects.annotate(orders=Count('order__id')).filter(orders__gt=5)
    # print(customers)

    # customers and the total amount they have spent
    # total_amount_spent = Sum(F('order__orderitem__quantity') * F('order__orderitem__unit_price'))
    # customers = Customer.objects.annotate(total_amount_spent=total_amount_spent)
    # print(customers)

    # top 5 best selling products and their total sales
    # total_amount_spent = Sum(F('orderitem__quantity') * F('orderitem__unit_price'))
    # products = Product.objects.annotate(total_sales=total_amount_spent).order_by('-total_sales')[:5]
    # print(products)
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     order_item = OrderItem()
    #     order_item.order = order
    #     order_item.product_id = 1
    #     order_item.quantity = 10
    #     order_item.unit_price = 20.34
    #     order_item.save()

    return render(request, "hello.html")
