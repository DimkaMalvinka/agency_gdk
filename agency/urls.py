from django.conf.urls import patterns, include, url
from django.contrib import admin
from neruhomist import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agency.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^object/(?P<h_id>\d+)/$', views.object, name='object'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
	url(r'^poslugi/$', views.poslugi, name='poslugi'),
	url(r'^karta/$', views.karta, name='karta'),
	url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^filtration/$', views.filtration, name='filtration'),
    url(r'^kvarturu/orenda/$', views.kvOrenda, name='kvOrenda'),
	url(r'^kvarturu/prodaj/$', views.kvProdaj, name='kvProdaj'),
	url(r'^budinki/orenda/$', views.budOrenda, name='budOrenda'),
	url(r'^budinki/prodaj/$', views.budProdaj, name='budProdaj'),
	url(r'^comercial/orenda/$', views.comOrenda, name='comOrenda'),
	url(r'^comercial/prodaj/$', views.comProdaj, name='comProdaj'),
	url(r'^zamiska/orenda/$', views.zamOrenda, name='zamOrenda'),
	url(r'^zamiska/prodaj/$', views.zamProdaj, name='zamProdaj'),
	url(r'^dilyanku/orenda/$', views.dilOrenda, name='dilOrenda'),
	url(r'^dilyanku/prodaj/$', views.dilProdaj, name='dilProdaj'),
	url(r'^inshe/orenda/$', views.inOrenda, name='inOrenda'),
	url(r'^inshe/prodaj/$', views.inProdaj, name='inProdaj'),
    
)
