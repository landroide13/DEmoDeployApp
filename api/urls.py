from rest_framework import routers

from api.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls


