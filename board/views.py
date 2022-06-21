from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'board/list.html')


def view(request):
    return render(request, 'home/view.html')


def write(request):
    return render(request, 'member/write.html')