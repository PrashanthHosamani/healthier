from rest_framework.routers import (DefaultRouter)

from .views import (PatientDoctorMappingViewSet)
router = DefaultRouter()

router.register("mappings", PatientDoctorMappingViewSet, basename="mappings")
urlpatterns = router.urls