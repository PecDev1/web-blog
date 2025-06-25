from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # <--- BU SHART!
    path('admin_tools_stats/', include('admin_tools_stats.urls')),

    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
    path('', include('news.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),

]

# Media va static fayllar uchun URL konfiguratsiyasi
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
