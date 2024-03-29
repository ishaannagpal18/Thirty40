
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns

from django.views.static import serve
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('contactus/', include('contact.urls')),
    path('account/', include('App_Login.urls')),
    path('blog/', include('Blog.urls')),
    # path('education/', include('Education.urls')),
    path('tennis-consultancy/', include('Sports.urls')),
    path('', include('Tennis.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
