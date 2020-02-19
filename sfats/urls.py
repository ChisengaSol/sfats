"""sfats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from users.views import UserViewSet, UserProfileViewSet, UserRegistrationView, UserLoginView
from schedule.views import ScheduleViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profile', UserProfileViewSet)
router.register(r'schedule', ScheduleViewSet)
# router.register(r'login', UserLoginView.as_view)
# router.register(r'api/token', TokenObtainPairView.as_view())
# router.register(r'api/token/refresh', TokenRefreshView.as_view())

urlpatterns = [
    url(r'^login', UserLoginView.as_view()),
    url(r'^signup', UserRegistrationView.as_view()),
    # path('api/', include(users.urls)),
    path('api', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view())
       
]
