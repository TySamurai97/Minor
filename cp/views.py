from django.shortcuts import render
from rest_framework import response
from django.http import HttpResponse
from django.template import RequestContext
import cp.crawler.cf as cf
import cp.crawler.spj as spj
import queries as q
import simplejson as jsn
import cp.crawler.calander as cl


#  192.168.43.190:8000/cp/spoj?handle=ty_samurai97&uname=tanay
#  192.168.43.190:8000/cp/codeforces?handle=cool_head&uname=tanay
#  ip:port/cp/register?uname=tanay&spjHandle=abc&cfHandle=abc

def register(request):
	uname = request.GET['uname']
	spjHandle = request.GET['spjHandle']
	cfHandle = request.GET['cfHandle']
	return HttpResponse(request.path)



def spojToJson(request):
    handle = request.GET['handle']
    uname = request.GET['uname']
    resultSet = q.getSPOJresult(handle)
    if(len(resultSet)==0):
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
	handle = request.GET['handle']
	uname = request.GET['uname']
	resultSet = q.getCodeForcesresult(handle)
	if(len(resultSet)==0):
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