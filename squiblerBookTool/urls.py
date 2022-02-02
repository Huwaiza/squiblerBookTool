from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Squibler books API",
      default_version='v1',
      description="API endpoints for squibler book tool",
      contact=openapi.Contact(email="muhammadhuwaizatahir@gmail.com"),
      license=openapi.License(name="Squibler License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('books/', include('nesting_books.urls')),
]
