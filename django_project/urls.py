from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from django_project import settings

urlpatterns = i18n_patterns(
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('admin/', admin.site.urls),
    # path('', include('my_django_app.urls')),
    # prefix_default_language=False
)

urlpatterns += [
    # Django's 'set_language' view, for the language switcher redirection
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Cpanel"
admin.site.site_title = "Cpanel"
admin.site.index_title = "Cpanel"
