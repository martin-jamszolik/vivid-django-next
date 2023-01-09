from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>/', views.project_details, name='project_details'),
]