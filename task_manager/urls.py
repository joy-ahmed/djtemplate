
from django.contrib import admin
from django.urls import path
from task_app.views import *

urlpatterns = [
    path('', index, name="index"), 
    path('todolist/', todolist, name="todolist"), 
    path('contact/', contact, name="contact"), 
    path('admin/', admin.site.urls),
]
