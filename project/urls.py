from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView



urlpatterns = [
    #main
    path('admin/', admin.site.urls),
    #users app
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #show app
    path('shows/', include('shows.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
