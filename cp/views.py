from django.shortcuts import render
from rest_framework import response
from django.http import HttpResponse
from django.template import RequestContext
import cp.crawler.cf as cf
import cp.crawler.spj as spj
import cp.crawler.cfRating as cfRating
import queries as q
import simplejson as jsn
import cp.crawler.calander as cl


#  192.168.43.190:8000/cp/spoj?handle=ty_samurai97&uname=tanay
#  192.168.43.190:8000/cp/codeforces?handle=cool_head&uname=tanay
#  ip:port/cp/register/?uname=tanay&spjHandle=abc&cfHandle=abc&ccHandle=abd
#  ip:port/cp/compare/?uname=tanay

def register(request):
	uName = request.GET['uname']
	spjHandle = request.GET.get('spjHandle')
	cfHandle = request.GET.get('cfHandle')
	if(not cfHandle is None ):
		codefRating = cfRating.getCfRating(cfHandle.strip())
	q.addUserData(uName,spjHandle,cfHandle,codefRating)
	return HttpResponse(jsn.dumps({'cfRating':codefRating}), content_type="application/json")

def compare(request):
	uName = request.GET.get('uname')
	return HttpResponse(jsn.dumps( q.getComparisionData(uName) ), content_type="application/json")


def spojToJson(request):
    handle = request.GET.get('handle')
    uname = request.GET.get('uname')
    resultSet = q.getSPOJresult(handle)
    if(len(resultSet)==0):
	    uname = uname.split('=')[-1]
	    problemList = spj.createList(handle)
	    uData = q.getUserFromName(uname)

	    for problem in problemList:
	    	q.addSPOJ(uData,handle,problem[0],problem[1],problem[2])
	    	for tag in problem[3]:
	    		q.addProblem(problem[1],tag)
	    resultSet = q.getSPOJresult(handle)

    responseData = []
    for problem in resultSet:
    	responseData.append({ 'title':problem[0].problemTitle,'link':problem[0].problemLink,'success':problem[0].success,'tags':problem[1] })
    return HttpResponse(jsn.dumps(responseData), content_type="application/json")


def codeforcesToJson(request):
	handle = request.GET.get('handle')
	uname = request.GET.get('uname')
	resultSet = q.getCodeForcesresult(handle)
	if(len(resultSet)==0):
		uname = uname.split('=')[-1]
		problemList = cf.createList(handle)
		uData = q.getUserFromName(uname)
		
		for problem in problemList:
			q.addCodeForces(uData,handle,problem[0],problem[1],problem[2])
			for tag in problem[3]:
				q.addProblem(problem[1],tag)
		resultSet = q.getCodeForcesresult(handle)

	responseData = []
	for problem in resultSet:
		responseData.append({ 'title':problem[0].problemTitle,'link':problem[0].problemLink,'success':problem[0].success,'tags':problem[1] })
	return HttpResponse(jsn.dumps(responseData), content_type="application/json")