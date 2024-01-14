from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/about_us/', include("apps.About_us.urls")),
                  path('api/v1/sendmessage/', include("apps.ContactUsMessage.urls")),
                  path('api/v1/service/', include("apps.Services.urls"))
              ] + urls_swagger
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
