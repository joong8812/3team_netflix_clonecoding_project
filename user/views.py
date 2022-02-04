from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model #사용자가 데이터베이스 안에 있는지 검사하는 함수


# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        profilename = request.POST.get('profile-name','')

        exist_user = get_user_model().objects.filter(email=email)
        if exist_user:
            return render(request, 'user/signup.html')
        else:
            UserModel.objects.create_user(email=email, password=password, username=profilename)
            return redirect('/sign-in')

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)

        me = UserModel.objects.get(username=username)
        if me.password == password:
            request.session['user'] = me.username
            return HttpResponse("로그인 성공!")
        else:
            return redirect('/login')

    elif request.method == 'GET':
        return render(request, 'login/login.html')