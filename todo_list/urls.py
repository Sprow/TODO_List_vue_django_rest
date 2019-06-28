from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^todo_list/', include('task.urls')),
    url(r'^docs/', include_docs_urls(title='API Documentation')),
]
