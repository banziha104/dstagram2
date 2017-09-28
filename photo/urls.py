from django.conf.urls import url
from django.views.generic import DetailView
from .models import Photo
from . import views

urlpatterns = [
    url(r'^$',views.post_list, name='post_list'),
    url(r'^single/(?P<pk>\d+)/$', DetailView.as_view(model=Photo,template_name='photo/detail.html'),name='post_detail'),
    url(r'^upload/$',views.UploadView.as_view(), name='post_create'),
    url(r'^delete/(?P<pk>\d+)/$',views.PhotoDeleteV.as_view(),name='post_delete')
]