from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSiteViewSet, UserProfileViewSet, proxy_view

router = DefaultRouter()
router.register(r'user-sites', UserSiteViewSet)
router.register(r'user-profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<str:site_name>/', proxy_view),
]
