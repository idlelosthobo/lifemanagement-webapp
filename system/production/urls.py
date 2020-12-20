from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.landing.urls')),
    path('accounts/', include('app.registration.urls')),
    path('admin/', admin.site.urls),
    path('welcome/', include('app.welcome.urls')),
]
