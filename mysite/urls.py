from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('physics.urls')),
    url(r'^users/', include('physics.urls', namespace='physics')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
