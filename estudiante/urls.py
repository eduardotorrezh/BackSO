from rest_framework import routers
from .viewsets import EstudianteViewSet

router = routers.SimpleRouter()
router.register('estudiantes', EstudianteViewSet)

urlpatterns = router.urls