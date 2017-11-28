import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','noobTopro.settings')
import django
django.setup()
from cp.models import UserData, SPOJ, CodeForces ,Problems, UserStats
from collections import Counter

tagClass = [['implementation','ad-hoc','ad-hoc-1','brute force'],
	['binary search','binary-search'],
	['dp','dynamic-programming'],
	['game-theory','games','game','game-theory-1'],
	['graphs','graph-theory','graph','trees','tree','dfs and similar','dfs','bfs','dijkstra-s-algorithm','shortest-path'],
	['greedy','sorting','sortings'],
	['hashing'],
	['math','maths','simple-math','number-theory','number theory'],
	['string','strings'],
	['data structures','dsu']]

tagClassName = {'implementation':0,
	'binary search':1,
	'dp':2,
	'game-theory':3,
	'graphs':4,
	'greedy':5,
	'hashing':6,
	'math':7,
	'string':8,
	'data structures':9}
tagClassNameList = ['implementation','binary_search','dp','game_theory','graphs','greedy','hashing','math','string','data_structures']

def addUserData(userName, spojHandle, spojRating, codeforcesHandle, codeforcesRating):

	ud = UserData.objects.get_or_create(userName = userName.strip(),spojHandle = spojHandle,
		spojRating = spojRating,codeforcesHandle = codeforcesHandle,codeforcesRating = codeforcesRating)[0]
	ud.save()
	return ud

def addUserStats(userData, userName, implementation ,binarySearch ,dp
	,gameTheory ,graphs ,greedy ,hashing ,math ,string ,dataStructures):

	ud = UserStats.objects.get_or_create(userData = userData,userName = userName,
		implementation = implementation ,binarySearch = binarySearch,
		dp = dp,gameTheory = gameTheory,graphs = graphs,greedy = greedy,
		hashing = hashing,math =math,string = string,dataStructures = dataStructures)[0]
	
	ud.save()
	return ud

def getUserFromName(name):
	ud = UserData.objects.filter(userName = name.strip())
	return ud[0]

def addCodeChef(userdata,handle,link,title,success):
	entry = CodeChef.objects.get_or_create(userdata = userdata,userHandle = handle,problemLink = link,problemTitle = title,success = success)[0]
	entry.save()
	return entry

def addSPOJ(userdata,handle,link,title,success):
	entry = SPOJ.objects.filter(userdata = userdata,userHandle = handle,problemLink = link,problemTitle = title,success = success)
	if( len(entry) == 0 ):
		entry = SPOJ.objects.get_or_create(userdata = userdata,userHandle = handle,problemLink = link,problemTitle = title,success = success)[0]
		entry.save()
	return entry

def addCodeForces(userdata,handle,link,title,success):
	entry = CodeForces.objects.filter(userdata = userdata,userHandle = handle,problemLink = link,problemTitle = title,success = success)
	if( len(entry) == 0 ):
		entry = CodeForces.objects.get_or_create(userdata = userdata,userHandle = handle,problemLink = link,problemTitle = title,success = success)[0]
		entry.save()
	return entry

def getCodeForcesresult(handle):
	probList = CodeForces.objects.filter(userHandle = handle)
	ls = []
	for problem in probList:
		ls.append([ problem, getTagsFromProblem(problem.problemTitle) ])
	return ls

def getSPOJresult(handle):
	probList = SPOJ.objects.filter(userHandle = handle)
	ls = []
	for problem in probList:
		ls.append([ problem, getTagsFromProblem(problem.problemTitle) ])
	return ls

def addProblem(title,tag):
	entry = Problems.objects.filter(problemTitle = title,tag = tag)
	if( len(entry) == 0 ):
		entry = Problems.objects.get_or_create(problemTitle = title, tag = tag)[0]
		entry.save()
	return entry

def getTagsFromProblem(title):
	resultSet = Problems.objects.filter(problemTitle = title)
	taglist = []
	for qset in resultSet:
		taglist.append(qset.tag)
	return taglist

def getComparisionData(userName):
	resultSet = getUserFromName(userName)
	problemList = []
	tagCount = [0 for _ in range(len(tagClass))]
	
	if(not resultSet.spojHandle is None):
		result = getSPOJresult(resultSet.spojHandle)
		for prob in result:
			vis = [0 for _ in range(len(tagClass))]
			# print(prob[1])
			for tag in prob[1]:
				for i in range(len(tagClass)):
					if tag in tagClass[i] and (vis[ tagClassName[ tagClass[i][0] ] ]==0):
						vis[ tagClassName[ tagClass[i][0] ] ] = 1
						tagCount[i]+=1


	if(not resultSet.codeforcesHandle is None):
		result = getCodeForcesresult(resultSet.codeforcesHandle)
		for prob in result:
			vis = [0 for _ in range(len(tagClass))]
			# print(prob[1])
			for tag in prob[1]:
				for i in range(len(tagClass)):
					if tag in tagClass[i] and (vis[ tagClassName[ tagClass[i][0] ] ]==0):
						vis[ tagClassName[ tagClass[i][0] ] ] = 1
						tagCount[i]+=1

	ansDist = []
	for i in range(len(tagCount)):
		ansDist.append({ 'type':tagClassNameList[i], 'count':tagCount[i]})
	return ansDist

if __name__ == '__main__':
	print(getComparisionData('tanay'))