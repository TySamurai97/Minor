from django.conf.urls import url
from cp import views

urlpatterns = [url(r'^spoj/', views.spojToJson , name='spojToJson'),
				url(r'^codeforces/', views.codeforcesToJson , name='codeforcesToJson'),
				url(r'^register/', views.register , name='register'),
				url(r'^compare/', views.compare , name='compare'),
				url(r'^sortUsers/', views.sortUsers , name='sortUsers'),
				url(r'^getCal/', views.getCal , name='getCal'),
				url(r'^getUserProfileData/', views.getUserProfileData , name='getUserProfileData'),
				url(r'^getUnsolvedList/', views.getUnsolvedList , name='getUnsolvedList'),]