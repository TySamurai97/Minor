import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','noobTopro.settings')
import django
django.setup()
from cp.models import UserData, SPOJ, CodeForces, UserHandle


def addUserData(name,password,email,mobno,gender,corc,year):
	ud = UserData.objects.get_or_create(userName = name.strip(),passWord = password.strip(),userEmail = email.strip(),mobileNo = mobno.strip(),Gender = gender.strip(),collageOrCompany = corc.strip(),year = year.strip())[0]
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
	entry = SPOJ.objects.get_or_create(userdata = userdata,userHandle = handle,problemLink = link,problemTitle = title,success = success)[0]
	entry.save()
	return entry


def addCodeForces(userdata,handle,link,title,success):
	entry = CodeForces.objects.get_or_create(userdata = userdata,userHandle = handle,problemLink = link,problemTitle = title,success = success)[0]
	entry.save()
	return entry

def addUserHandle(codechefHandle,spojHandle,codeforcesHandle,codechefRating,spojRating,codeforcesRating):
	entry = UserHandle.objects.get_or_create(codechefHandle = codechefHandle,spojHandle = spojHandle,codeforcesHandle = codeforcesHandle,codechefRating = codechefRating,spojRating = spojRating,codeforcesRating = codeforcesRating)[0]
	entry.save()
	return entry

def getCodeForcesresult(handle):
	return CodeForces.objects.filter(userHandle = handle)

def getSPOJresult(handle):
	return SPOJ.objects.filter(userHandle = handle)


if __name__ == '__main__':
	#x = addUserData('ayush','134','asssc@gmail.com','8354038899','m','JIIT','2019')
	#addCodeChef(x,'ayush333','asd@gmail.com','abc',1)
	#addUserHandle('ab','abc','abcd',1200,1500,1900)
	print(getCodeForcesresult('cool_head'))