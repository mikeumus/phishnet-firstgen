from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrapy_phishtank.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

## http://stackoverflow.com/a/24983231/1762493
admin.site.site_header = 'PhishNet Admin'