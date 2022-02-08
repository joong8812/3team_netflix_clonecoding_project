from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model #사용자가 데이터베이스 안에 있는지 검사하는 함수
import json
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        profilename = request.POST.get('profile-name', '')

        if email == '' or password == '' or profilename == '':
            return render(request, 'user/signup.html', {'error': '이메일과 패스워드, 프로필 이름은 필수 값 입니다'})
        elif len(password) < 5:
            return render(request, 'user/signup.html', {'error': '패스워드는 다섯글자 이상입니다'})
        elif len(profilename) < 3:
            return render(request, 'user/signup.html', {'error': '프로필 이름은 세글자 이상입니다'})

        exist_user = get_user_model().objects.filter(email=email)
        if exist_user:
            return redirect('/login')
        else:
            UserModel.objects.create_user(email=email, password=password, username=profilename)
            return redirect('/login')


# genre 판별
@login_required
def genre(request):
    if request.method == "POST":
        genre_list = request.POST.get('genre_list')
        genre_list = genre_list.split(',')
        g = [g.split('_')[1] for g in genre_list]
        g_last = json.dumps(g)

        me = request.user
        me.genre_list= g_last
        me.save()
        return redirect('/main_page')

    elif request.method == 'GET':
        return render(request, 'user/genre.html')
