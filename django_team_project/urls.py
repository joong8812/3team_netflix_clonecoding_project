"""django_team_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from . import views
from .views import CustomSignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    re_path(r'^accounts/social/signup/$', CustomSignupView.as_view(), name='socialaccount_signup'), # 소셜로그인 시, 다른 플래폼에 이미 해당 이메일로 회원가입 되어있는 경우 타는 url
    path('accounts/',include('allauth.urls')),  # allauth 관련 페이지 route
    path('', include('user.urls')),

]
