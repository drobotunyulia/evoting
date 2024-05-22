from django.contrib import admin
from django.urls import path, include

from main.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('', include('main.urls')),
]


handler404 = page_not_found
