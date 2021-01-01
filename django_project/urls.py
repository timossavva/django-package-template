from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from django_project import settings
from django_project.settings import PREFIX_DEFAULT_LANGUAGE

urlpatterns = i18n_patterns(
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    prefix_default_language=False
)

urlpatterns += [
    path('admin/', admin.site.urls),
    path('config-dyna-builder/', include('config_dyna_builder.urls')),
    # Django's 'set_language' view, for the language switcher redirection
    path('i18n/', include('django.conf.urls.i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Cpanel"
admin.site.site_title = "Cpanel"
admin.site.index_title = "Cpanel"
