from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render(request, 'login/login.html')