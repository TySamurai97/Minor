from django.shortcuts import render
import _thread as thrd
from rest_framework import response
from django.http import HttpResponse
from django.template import RequestContext
import cp.crawler.cf as cf
import cp.crawler.spj as spj
import cp.crawler.cfRating as cfRating
import cp.crawler.SpojRanking as spjRating
import queries as q
import simplejson as jsn
import cp.crawler.cal as cl


#  192.168.43.190:8000/cp/spoj?handle=ty_samurai97&uname=tanay
#  192.168.43.190:8000/cp/codeforces?handle=cool_head&uname=tanay
#  ip:port/cp/register/?uname=tanay&spjHandle=abc&cfHandle=abc
#  ip:port/cp/compare/?uName1=tanay&uName2=aditya
#  ip:port/cp/sortUsers/?tag=dp
#  ip:port/cp/getCal
#  ip:port/cp/getUserProfileData/?uName=tanay

def getCal(request):
	return HttpResponse(jsn.dumps(cl.getCal()), content_type="application/json")

def sortUsers(request):
	tagName = request.GET['tag']
	return HttpResponse(jsn.dumps(q.getSortedUsersOnTags(tagName.strip())), content_type="application/json")

def gatherData(userData,uname,spjHandle,cfHandle):
	resultSet = q.getSPOJresult(spjHandle)
	if(len(resultSet)==0):
		problemList = spj.createList(spjHandle)
		uData = q.getUserFromName(uname)
		for problem in problemList:
			q.addSPOJ(uData,spjHandle,problem[0],problem[1],problem[2])
			for tag in problem[3]:
				q.addProblem(problem[1],tag)

	resultSet = q.getCodeForcesresult(cfHandle)
	if(len(resultSet)==0):
		problemList = cf.createList(cfHandle)
		uData = q.getUserFromName(uname)
		for problem in problemList:
			q.addCodeForces(uData,cfHandle,problem[0],problem[1],problem[2])
			for tag in problem[3]:
				q.addProblem(problem[1],tag)

	tagList = q.getComparisionData(uname)
	q.addUserStats(userData, uname, tagList[0]['count'] ,tagList[1]['count'] ,tagList[2]['count']
		,tagList[3]['count'] ,tagList[4]['count'] ,tagList[5]['count'] ,tagList[6]['count']
		,tagList[7]['count'] ,tagList[8]['count'] ,tagList[9]['count'])

def register(request):
	uName = request.GET['uname']
	spjHandle = request.GET.get('spjHandle')
	cfHandle = request.GET.get('cfHandle')
	if (cf.verifyCF(cfHandle) and spj.validateSpoj(spjHandle) ):

		codefRating = spojRating = ""
		if(not cfHandle is None ):
			codefRating = cfRating.getCfRating(cfHandle.strip())
		if(not spjHandle is None ):
			spojRating = spjRating.spojRank(spjHandle.strip())
		# print("\n\n\n" + spojRating + "\n\n\n")
		userdata = q.addUserData(uName,spjHandle,spojRating,cfHandle,codefRating)
		# start new thread to perform crawling and heavy computations
		thrd.start_new_thread(gatherData, (userdata,uName,spjHandle,cfHandle) )
		
		return HttpResponse(jsn.dumps({'cfRating':codefRating,'spjRating':spojRating}), content_type="application/json")

	return HttpResponse(jsn.dumps({'cfRating':'error','spjRating':'error'}), content_type="application/json")


def spojToJson(request):
    handle = request.GET.get('handle')
    uname = request.GET.get('uname')
    resultSet = q.getSPOJresult(handle)
    if(len(resultSet)==0):
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

def compare(request):
	uName1 = request.GET.get('uName1')
	uName2 = request.GET.get('uName2')
	return HttpResponse(jsn.dumps( {'uName1':q.getComparisionData(uName1),'uName2':q.getComparisionData(uName2)} ), content_type="application/json")

def getQList(uname):
	uData = q.getUserFromName(uname)
	spjHandle = uData.spojHandle
	resultSet = q.getSPOJresult(spjHandle)
	responseData = []
	for problem in resultSet:
		responseData.append({ 'title':problem[0].problemTitle,'link':problem[0].problemLink,'success':problem[0].success,'tags':problem[1] })
	cfHandle = uData.codeforcesHandle
	resultSet = q.getCodeForcesresult(cfHandle)
	for problem in resultSet:
		responseData.append({ 'title':problem[0].problemTitle,'link':problem[0].problemLink,'success':problem[0].success,'tags':problem[1] })
	return responseData

def getUserProfileData(request):
	uName = request.GET.get('uName')
	return HttpResponse(jsn.dumps( {'usrstats':q.getComparisionData(uName),'qSolved':getQList(uName)} ), content_type="application/json")