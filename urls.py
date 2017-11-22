from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='accueil'),
    url(r'^connection/$', views.connection, name='connection'),
    url(r'^refresh/$', views.refresh, name = 'refresh'),
    url('^new_mdp/$', views.new_mdp, name = 'new_mdp'),
    url('^finalcountdown/$', views.finalcountdown, name='finalcountdown'),
    url('^lolz/$', views.lolz, name='lolz'),
]
