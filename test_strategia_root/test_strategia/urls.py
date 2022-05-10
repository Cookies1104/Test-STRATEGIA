from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


api_url = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{api_url}', include('article.urls')),
    path('api/schema/download/', SpectacularAPIView.as_view(), name='schema'),
    path('users/', include('users.urls')),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
