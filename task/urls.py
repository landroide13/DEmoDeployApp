from django.urls import path, include
from home import views

urlpatterns = [
    path('tasks/', views.render_articles, name='tasks'),
]