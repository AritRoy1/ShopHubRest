
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
 
# from rest_framework_swagger.views import get_swagger_view
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_swagger_view(title='ShopHub Rest Api')

# schema_view = get_schema_view(
#     openapi.Info(
#         title="ShopHub Rest Api",
#         default_version='v1',),
#     public=True,
    
# )
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', include('customer.urls')),
    path('product/', include('product.urls')),
    path('rating/', include('rating.urls')),
    # path('apidocs/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
