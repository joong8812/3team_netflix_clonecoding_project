from django.shortcuts import render

# Create your views here.
def index_view(request):
    if request.method == 'GET':
        return render(request, 'index/index.html')