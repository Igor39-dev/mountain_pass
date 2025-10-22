from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from perevalapp.views import PerevalViewSet
from .yasg import urlpatterns as yasg_urlpatterns

router = DefaultRouter()
router.register('pereval', PerevalViewSet, basename='pereval')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

urlpatterns += yasg_urlpatterns