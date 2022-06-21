from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'member/join.html')


def view(request):
    return render(request, 'member/login.html')


def write(request):
    return render(request, 'member/myinfo.html')