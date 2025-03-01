from django.urls import path, include
from task import views

urlpatterns = [
    path('', views.render_tasks, name='tasks'),
]