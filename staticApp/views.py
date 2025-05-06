from django.shortcuts import render

def home_view(request):
    context = {
        "username": "John",
        "fruits": ["Apple", "Banana", "Mango"],
        "is_logged_in": True,
    }
    return render(request, 'base.html', context)
