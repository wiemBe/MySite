
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("blog/", include("blog.urls")), already directing this url below. Doing the same thing 
    path("", include("blog.urls"))
]


