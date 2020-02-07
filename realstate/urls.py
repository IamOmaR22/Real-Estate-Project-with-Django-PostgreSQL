from django.contrib import admin
from django.urls import path, include
from django.conf import settings            ## Media Folder
from django.conf.urls.static import static  ## Media Folder



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       ## Media Folder
