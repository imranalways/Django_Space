from django.conf.urls import url
from PostApp import views

urlpatterns=[
    url(r'^post/$',views.PostApi),
    url(r'^post/<str:PostId>',views.PostApi)
]