from django.conf.urls.defaults import *
import recipes
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^cookbook/', include('cookbook.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

    (r'^welcome$', 'recipes.views.welcome'),
    (r'^%s/(?
P<path>.*)$' % recipes.MEDIA_URL, 'django.views.static.serve', {'document_root': recipes.MEDIA_ROOT})
))
)
