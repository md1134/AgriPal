from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),               # home page
    path('farm/<int:farm_id>/', views.farm_env_data, name='farm_env_data'),  # form page
]