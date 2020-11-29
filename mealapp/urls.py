from django.urls import path
from . import views
urlpatterns = [
    path('', views.ajax_form),
    path('advance/', views.avance_form),
]