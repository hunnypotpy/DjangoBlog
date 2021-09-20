from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('my_backend/', admin.site.urls),
]