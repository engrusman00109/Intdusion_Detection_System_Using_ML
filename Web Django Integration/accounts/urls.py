from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path("", HomeView.as_view()),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("allauth.socialaccount.urls")),
]
