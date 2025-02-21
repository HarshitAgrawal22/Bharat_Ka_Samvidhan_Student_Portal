from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("student.urls")),
    path("administration/", include("administration.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handle 404

handler404 = "accounts.views.page_not_found_view"
