from rest_framework.routers import DefaultRouter

from urbanwaveflair.store import views

router = DefaultRouter()
router.register("products", viewset=views.ProductViewSet)
router.register("collections", viewset=views.CollectionViewSet)

urlpatterns = router.urls
