from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .drf_yasg import urlpatterns as urls_swagger

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/about_us/', include("apps.About_us.urls")),
                  path('api/v1/products/', include("apps.Products.urls")),
                  path('api/v1/lesson/', include("apps.Lesson.urls")),
                  path('api/v1/group/', include("apps.Group.urls"))
              ] + urls_swagger
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
