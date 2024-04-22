from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Register URLs of our 'movies' app
    path('', include('apps.movies.urls')),
]

# This is not suitable for production!! 
# For more information on serving these files, see: 
# https://docs.djangoproject.com/en/1.11/howto/static-files/deployment/
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
