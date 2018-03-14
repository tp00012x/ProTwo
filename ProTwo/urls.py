from django.contrib import admin
from django.urls import path, include
from users_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', include('users_app.urls')),
    path('admin/', admin.site.urls),
]
