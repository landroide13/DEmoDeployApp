
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from home import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('tasks/', include('task.urls')),
    path('api/', include('api.urls')),
    path('auth/', obtain_auth_token),
]
