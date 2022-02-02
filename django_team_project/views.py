from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from allauth.socialaccount.views import SignupView


# 중복 이메일로 소셜 로그인하는 경우
class CustomSignupView(SignupView):
    http_method_names = ['get']

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        social_login_email: str = self.sociallogin.user.email

        messages.add_message(self.request, messages.WARNING, f"{social_login_email}")
        messages.add_message(self.request, messages.WARNING, '가입 된 기존 이메일과 중복 됩니다')
        messages.add_message(self.request, messages.WARNING, '이메일을 확인 해 주세요')

        return redirect("/login")
