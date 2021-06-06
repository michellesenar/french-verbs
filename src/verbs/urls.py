from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^enfr', views.randomizer, name='randomizer'),
    url(r'^about', views.about, name='about'),
    url(r'^conjugation/(?P<verb_pk>\d+)/$', views.conjugation, name='conjugation'),
    url(r'^memorize', views.memorize, name='memorize'),
]
