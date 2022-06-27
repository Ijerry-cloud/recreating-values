from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('men-wey-sabi/', admin.site.urls),
    path('homepage/', include('home.urls', namespace='home')),
    path('events/', include('events.urls', namespace='events')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('', include('home.urls', namespace='home')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)