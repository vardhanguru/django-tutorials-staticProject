from django.shortcuts import render

def home_view(request):
    context = {
        "username": "John",
        "fruits": ["Apple", "Banana", "Mango"],
        "is_logged_in": False,
    }
    return render(request, 'base.html', context)


def login_view(request):
    return render(request,'login.html')