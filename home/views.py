from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'home.html', {'active': 'home'})

def events(request):
    return render(request , 'events.html', {'active': 'events'})

def archive(request):
    return render(request , 'archive.html', {'active': 'archive'})

def about(request):
    return render(request , 'about.html', {'active': 'about'})