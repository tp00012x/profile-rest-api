from django.urls import path
from . import views

urlpatterns = [
    path(r'hello-view/', views.HelloApiView.as_view()),
]
