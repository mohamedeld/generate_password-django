from django.urls import path
from . import views
app_name='password'
urlpatterns = [
   path('',views.home,name='home'),
   path('password/',views.password,name='password'),
]