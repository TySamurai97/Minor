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


def spojToJson(request):
    url = request.path
    handle = url.split('/')[-1]
    handle,uname = handle.split('&')
    handle = handle.split('=')[-1]
    
    uname = uname.split('=')[-1]
    problemList = spj.createList(handle)
    uData = q.getUserFromName(uname)

    for problem in problemList:
    	q.addSPOJ(uData,handle,problem[0],problem[1],problem[2])
    resultSet = q.getSPOJresult(handle)
    responseData = []
    for problem in resultSet:
    	responseData.append({ 'title':problem.problemTitle,'link':problem.problemLink,'success':problem.success })
    return HttpResponse(jsn.dumps(responseData), content_type="application/json")


def codeforcesToJson(request):
	url = request.path
	handle = url.split('/')[-1]
	handle,uname = handle.split('&')
	handle = handle.split('=')[-1]
	uname = uname.split('=')[-1]
	problemList = cf.createList(handle)
	uData = q.getUserFromName(uname)
	
	for problem in problemList:
		q.addCodeForces(uData,handle,problem[0],problem[1],problem[2])
	
	resultSet = q.getCodeForcesresult(handle)
	responseData = []
	for problem in resultSet:
		responseData.append({ 'title':problem.problemTitle,'link':problem.problemLink,'success':problem.success })
	return HttpResponse(jsn.dumps(responseData), content_type="application/json")