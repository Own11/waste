"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
# pyrefly: ignore [missing-import]
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'outlets', views.OutletViewSet, basename='outlet')
router.register(r'senders', views.SenderUserViewSet, basename='sender')
router.register(r'write-offs', views.WriteOffRequestViewSet, basename='writeoff')
router.register(r'requests', views.ReviewRequestViewSet, basename='request')

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('api/token/', views.ObtainAuthTokenWithRole.as_view(), name='token_obtain'),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

