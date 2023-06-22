from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('info/<str:model_name>/<int:pk>/', views.info, name='info'),
]
