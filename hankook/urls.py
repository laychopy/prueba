from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.index', name='home'),
    # url(r'^hankook/', include('hankook.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
