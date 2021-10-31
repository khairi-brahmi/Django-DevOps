from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
urlpatterns = [
    path('api', include('api.urls')),
    path('admin/', admin.site.urls),
    path('openapi/', get_schema_view(
        title="Test APIs",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='doc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
