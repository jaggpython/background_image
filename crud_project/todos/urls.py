from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from django.urls import path, include
from .views import home

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todo')

urlpatterns = router.urls

urlpatterns = [
    path("", home, name='home'),
    path("", include(router.urls))
]
