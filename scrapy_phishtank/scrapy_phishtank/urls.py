from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrapy_phishtank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')), # https://docs.djangoproject.com/en/1.8/ref/contrib/admin/admindocs/#overview
    # https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#overriding-admin-templates
    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# https://docs.djangoproject.com/en/1.8/ref/contrib/admin/#adminsite-attributes
admin.site.site_header = 'PhishNet Admin'
admin.site.site_title = 'PhishNet Admin'
