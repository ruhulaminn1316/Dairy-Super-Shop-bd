from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # django-allauth (Google Login, Signup, Logout)
    path('accounts/', include('allauth.urls')),

    # Main app (home page, user pages)
    path('', include('app.urls')),

    # Custom admin panel
    path('adminpanel/', include('adminpanel.urls')),
]

# Media files (only for DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
