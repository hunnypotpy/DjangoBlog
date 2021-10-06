from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

static_patterns = static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('my_backend/', admin.site.urls),
] + static_patterns

#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
