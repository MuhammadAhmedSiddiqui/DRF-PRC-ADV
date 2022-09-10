from django.urls import path, include

app_name = "user"

urlpatterns = [
    path("", include("user.views.user_api.urls"))
]
