from rest_framework.routers import DefaultRouter
from lost_found.viewsets import LostViewSet, FoundViewSet

router = DefaultRouter()
router.register('lost_found', LostViewSet, basename='lost')
router.register('lost_found', FoundViewSet, basename='found')

urlpatterns = router.urls