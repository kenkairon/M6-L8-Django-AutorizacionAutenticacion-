from django.urls import path
# importante
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='auth_app/login.html'), name="login"),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
]