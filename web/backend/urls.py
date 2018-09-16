from django.urls import path
from . import views

urlpatterns = [
    path('api/recorder/', views.RecorderListCreate.as_view()),
]