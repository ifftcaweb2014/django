from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ifftca.views.home', name='home'),
    url(r'^/', include('web2014.urls')),

#     url(r'^admin/', include(admin.site.urls)),
)
