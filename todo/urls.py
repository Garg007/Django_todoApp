from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get/$', views.index, name='index'),
    url(r'^details/(?P<id>\w)/$', views.details, name='details'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^update/$', views.update, name='update'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login1, name='login'),
    url(r'^logout/$', views.logout1, name='logout'),
]
