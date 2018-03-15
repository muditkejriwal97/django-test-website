from django.urls import path, re_path
from . import views


urlpatterns = [
    #.com/music/
    path('', views.index, name='index'),

    #.com/music/10/
    re_path(r'^(?P<album_id_from_url>[0-9]+)/$', views.detail, name = 'detail'),
]
