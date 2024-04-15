from rest_framework import routers

from apps.students.views import StudentAPIViewSet, StudentProfileAPIViewSet


router = routers.DefaultRouter()

router.register('students', StudentAPIViewSet)
router.register('profile', StudentProfileAPIViewSet, basename='profile')


urlpatterns = router.urls
