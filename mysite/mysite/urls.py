from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]