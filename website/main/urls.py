from rest_framework import routers

from .views import SomeViewSet

router = routers.SimpleRouter()
router.register("thing", SomeViewSet)
urlpatterns = router.urls
