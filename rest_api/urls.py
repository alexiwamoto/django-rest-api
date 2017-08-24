from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    # url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    # url(r'^bucketlists/(?P<pk>[0-9]+)/$',
    #     DetailsView.as_view(), name="details"),
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    # url(r'^users/$', UserView.as_view(), name="users"),
    # url(r'users/(?P<pk>[0-9]+)/$',
    #     UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
    # url(r'^produtos/', ProdutoList.as_view(), name="produtos"),
    # url(r'produtos/(?P<pk>[0-9]+)/$', ProdutoDetail.as_view(), name="produto_detail"),
    url(r'^produtos/$', views.produto_list),
    url(r'^produtos/(?P<pk>[0-9]+)$', views.produto_detail),
    url(r'^fotos/$', views.foto_list),
    url(r'^fotos/(?P<pk>[0-9]+)$', views.foto_detail),
}

urlpatterns = format_suffix_patterns(urlpatterns)
