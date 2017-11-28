from django.conf.urls import url
from cp import views

urlpatterns = [url(r'^spoj/', views.spojToJson , name='spojToJson'),
				url(r'^codeforces/', views.codeforcesToJson , name='codeforcesToJson'),
				url(r'^register/', views.register , name='register'),
				url(r'^compare/', views.compare , name='compare'),]