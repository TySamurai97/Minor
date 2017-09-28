from django.shortcuts import render
from rest_framework import response
from django.http import HttpResponse
from django.template import RequestContext
import cp.crawler.cf as cf
import cp.crawler.spj as spj
import queries as q
import simplejson as jsn


#  127.0.0.1:8000/cp/spoj/handle=ty_samurai97&uname=tanay
#  127.0.0.1:8000/cp/codechef/handle=tanay&uname=tanay
#  127.0.0.1:8000/cp/codeforces/handle=cool_head&uname=tanay

def index(request):
	path = request.get_full_path()
	s = path.split('/')[-1]
	if(len(s)==0):
		return render(request,'cp/index.html')
	s = s.split('&')
	site = s[0].split('=')[-1]
	handle = s[1].split('=')[-1]
	dataList = []
	if site == 'SPOJ':
		dataList = spojToJson(handle)
		#return HttpResponse('got spoj')
	elif site == 'CodeForces':
		dataList = codeforcesToJson(handle)
		#return HttpResponse('got cf')
	return render(request,'cp/basic.html', { 'problem':dataList } )


def spojToJson(handle):

	resultSet = q.getSPOJresult(handle)
	if(len(resultSet)==0):
		problemList = spj.createList(handle)
		for problem in problemList:
			q.addSPOJ(handle,problem[0],problem[1],problem[2])
		resultSet = q.getSPOJresult(handle)
	responseData = []
	for problem in resultSet:
		responseData.append({ 'title':problem.problemTitle,'link':problem.problemLink,'success':problem.success })
	return responseData


def codeforcesToJson(handle):
	resultSet = q.getCodeForcesresult(handle)
	if(len(resultSet)==0):
		problemList = cf.createList(handle)
		for problem in problemList:
			q.addCodeForces(handle,problem[0],problem[1],problem[2])
		resultSet = q.getCodeForcesresult(handle)
	responseData = []
	for problem in resultSet:
		responseData.append({ 'title':problem.problemTitle,'link':problem.problemLink,'success':problem.success })
	
	#edit from this point
	return responseData