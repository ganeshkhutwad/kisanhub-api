from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from full_stack_assignment.weather import views

router = routers.DefaultRouter()
router.register(r'england/weather', views.EnglandWeatherView, basename='weather')
router.register(r'scotland/weather', views.ScotlandWeatherView, basename='weather')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
