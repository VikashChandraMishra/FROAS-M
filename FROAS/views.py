from django.shortcuts import  render


def home(request):
    response = {"success": True, "message": "home page"}
    return render(request, 'index.html', response)


def about(request):
    response = {"success": True, "message": "about page"}
    return render(request, 'about.html')
