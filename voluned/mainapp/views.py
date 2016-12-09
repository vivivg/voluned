from django.shortcuts import render

BASEPATH="mainapp/"

# Create your views here.
def index(request):
    context = {"BASEPATH" : BASEPATH}
    return render(request, 'mainapp/index.html', context)
