from django.contrib import admin
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template,redirect_to
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('celeryproject.celeryweb.views',
    url(r'^news/(?P<slug>[\w-]*)', 'news', name='news'),
    url(r'^tutorials/(?P<slug>[\w-]*)', 'tutorials', name='tutorials'),
    url(r'^community/', 'community', name='external_resources'),
    url(r'^profile/(?P<username>.+)/', 'user_profile', name='user_profile'),
        
    #AJAX
    url(r'^ajax/stackoverflowquestions/(?P<page_size>[0-9]+)/(?P<page>[0-9]+)/$',
        'stackoverflow_questions',
        name='stackoverflow_questions'),
    
    #REDIRECTS
    url(r'^docs/', redirect_to, {'url': 'http://docs.celeryproject.org/'}),
    
    #ADMIN          
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home', name='home'),
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT, 'show_indexes': True
        },),
   )