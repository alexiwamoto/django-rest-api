from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^get-token/', obtain_auth_token),
    url(r'^produtos/$', views.produto_list),
    url(r'^produtos/(?P<pk>[0-9]+)$', views.produto_detail),
    url(r'^fotos/$', views.foto_list),
    url(r'^fotos/(?P<pk>[0-9]+)$', views.foto_detail),
}

urlpatterns = format_suffix_patterns(urlpatterns)
