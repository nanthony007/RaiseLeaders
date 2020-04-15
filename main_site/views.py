from django.shortcuts import render

# Create your views here.


def index(request):
    nick = 'Coool kidd'
    return render(request, 'main_site/home.html', context={'person': nick})
