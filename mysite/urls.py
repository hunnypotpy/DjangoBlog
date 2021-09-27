from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('my_backend/', admin.site.urls),
    path('upload/', views.image_upload_view)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)