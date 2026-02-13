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

# Root URL configuration (project-level).
#
# Django checks URL patterns from top to bottom.
# - The first matching pattern is used.
# - path('', include('app.urls')) means "try app URLs for any incoming path"
#   at that point in the order. If app has no match, Django continues below.

urlpatterns = [
    # Django admin panel (uses admin site routing, not app/views.py).
    path('admin/', admin.site.urls),
    # Home page at '/'.
    path('', views.home, name="home"),

    # Include app-level URLs.
    # Example: if app/urls.py had path('about/', ...), '/about/' would be resolved there.
    # Current app/urls.py is intentionally minimal, so project-level routes below still handle requests.
    path('', include("app.urls")),

    # Project-level routes currently used by templates.
    path('login/', views.login, name="login"),
    path('input/', views.input_data, name="input_data"),
    path('student/', views.student_data, name="student_data"),
]

# During development, serve uploaded media files through Django.
# In production, media should be served by a web server or cloud storage.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
