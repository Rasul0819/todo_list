
from django.contrib import admin
from django.urls import path
from todo import views
urlpatterns = [
    path('admin/', admin.site.urls),

    #auth
    path('signup/',views.signupuser, name='signupuser')


    #todos
]
