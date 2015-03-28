from django.conf.urls import patterns, include, url
from django.contrib import admin
from portfolio import settings
from works import views as works_views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', works_views.home, name='home'),
    url(r'^works/$', works_views.works, name='works'),
    url(r'^single/$', works_views.single_work, name='single_work'),
    url(r'^contacts/$', works_views.contacts, name='contacts'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),
#    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
#    	{'document_root': settings.MEDIA_ROOT}),
#	url(r'^i18n/', include('django.conf.urls.i18n'),  name='set_language'),
)
