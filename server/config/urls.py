from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def index(request):
    return redirect('/admin')

urlpatterns = [
    path('admin', admin.site.urls),
    path('', index),
    path('api/', include('blog.urls'))
]
