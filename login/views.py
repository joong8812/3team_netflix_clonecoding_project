from django.shortcuts import render, redirect
from django.contrib import auth, messages




# Create your views here.
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        
        me = auth.authenticate(request, email=email, password=password)

        if me is not None:
            auth.login(request, me)
            if me.genre_list =="":
                return redirect('/genre')  # 로그인 후 유저네임을 응답한다
            else:
                return render(request, 'main_page.html')
        else:
            messages.add_message(request, messages.WARNING, '유저이름 혹은 패스워드를 확인 해 주세요')
            return render(request, 'login/login.html')

    elif request.method == 'GET':
            return render(request, 'login/login.html')