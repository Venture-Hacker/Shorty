from django.urls import path
from . import views

app_name = "shorty"

urlpatterns = [
    path("", views.home, name="home"),
    path("link/<str:code>/", views.detail, name="detail"),
    path("<str:code>/", views.go, name="go"),  # must be last
]
