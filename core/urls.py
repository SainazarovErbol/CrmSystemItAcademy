from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from core.admin import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.api_urls')),
    path('api-login/', include('rest_framework.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
