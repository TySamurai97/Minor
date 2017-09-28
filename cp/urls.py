from django.conf.urls import url
from cp import views

urlpatterns = [url(r'^', views.index , name='index'),
]