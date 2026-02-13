"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name ="home"), # Home page because path is '' . If we put path('home/', views.home, name="home"), then the home page will be at http://localhost:8000/home/ instead of http://localhost:8000/ . So we use path('', views.home, name="home") to make the home page at http://localhost:8000/ .
    path('', include("app.urls")), # If we don't include this, then the urls in app/urls.py won't work django will only look for urls in djangoproject/urls.py
                                   # So we include the urls in app/urls.py by using path('', include("app.urls")) . This means that any url that starts with '' (which is all urls) will be handled by the urls in app/urls.py . So if we have path('login/', views.login, name="login") in app/urls.py , then the url http://localhost:8000/login/ will be handled by the login view in app/views.py .
                                   # If we have path('input/', views.input_data, name="input_data") in app/urls.py , then the url http://localhost:8000/input/ will be handled by the input_data view in app/views.py .
    path('login/', views.login, name="login"),
    path('input/', views.input_data, name="input_data")   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
