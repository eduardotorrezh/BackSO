from rest_framework import routers
from .viewsets import CarreraViewSet

router = routers.SimpleRouter()
router.register('carreras', CarreraViewSet)

urlpatterns = router.urls