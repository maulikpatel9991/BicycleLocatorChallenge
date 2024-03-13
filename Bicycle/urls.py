"""
URL configuration for Bicycle project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import locate_bicycle, bicycle_locator_data

urlpatterns = [
    path('data/', bicycle_locator_data, name='bicycle_locator_data'),
    path('admin/', admin.site.urls),
    path('locate_bicycle/', locate_bicycle, name='locate_bicycle'),

]
# http://127.0.0.1:8000/locate_bicycle/?latitude=20&longitude=20