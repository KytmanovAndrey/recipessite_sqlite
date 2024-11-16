from django.urls import path

from .views import registration_view, login_view, logout_view

urlpatterns = [
    path('registration/', registration_view, name='registration_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]
