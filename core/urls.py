from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path('complete/<int:pk>/', views.complete, name="complete"),
    path('delete/<int:pk>/', views.delete, name="delete")
]
