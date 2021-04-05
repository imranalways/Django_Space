from django.conf.urls import url
from PostApp import views

urlpatterns=[
    url(r'^post/$',views.PostApi)
]