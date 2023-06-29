from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('register/', views.register, name='register')
]
