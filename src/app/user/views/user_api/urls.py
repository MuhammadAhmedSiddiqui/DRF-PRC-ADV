from django.urls import path, include

from rest_framework.routers import DefaultRouter

from user.views.user_api import views

router = DefaultRouter()
router.register("", views.UserModelViewSet, "create")

urlpatterns = [
    path("", include(router.urls))
]
