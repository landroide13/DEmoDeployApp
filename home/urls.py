
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.render_articles, name='home'),
]