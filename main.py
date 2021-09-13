from django.contrib import admin
from django.urls import include, pathlib
urlpatterns = [
    path('', include('blog.urls')),
    path('my_backend/', admin.site.urls),
]