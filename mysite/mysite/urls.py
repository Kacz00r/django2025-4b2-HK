from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.landingpage, name="landingpage"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]