
from django.urls import path
from staticApp.views import home_view, login_view
urlpatterns = [
    path('first/', home_view),
    path('login',login_view, name='login')
]
