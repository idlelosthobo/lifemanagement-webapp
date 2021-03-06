from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.landing.urls')),
    path('', include('system.base_urls')),
    path('admin/', admin.site.urls),
    path('app/', include('app.core.urls')),
    path('app/accounts/', include('app.registration.urls')),
    path('app/welcome/', include('app.welcome.urls')),
    path('app/people/', include('app.people.urls')),
    path('app/note/', include('app.note.urls')),
]
