from django.urls import re_path
from . import views

app_name = 'polls'

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^(?P<question_id>[0-9]+)/$', views.details, name="details"),
    re_path(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    re_path(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
]
