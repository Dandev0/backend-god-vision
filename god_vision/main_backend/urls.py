from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HtmlPage().page),
    path('api/v1/camera_list/', views.CameraBase.as_view()),
    path('api/v1/logs/logs_services', views.Logs_services.as_view()),
    path('api/v1/start_camera/', views.validator_data),
    path('api/v1/restreaming/', views.restream_service_api),
]
