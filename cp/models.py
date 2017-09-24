from django.db import models

# Create your models here.
class UserData(models.Model):
	userId = models.IntegerField(default = 0,unique = True)
	userName = models.CharField(max_length = 128)
	passWord = models.CharField(default = 0)
	userEmail = models.URLField()
	mobileNo = models.CharField(max_length = 128)
	Gender = models.CharField(max_length = 1)
	collageOrCompany = models.CharField(max_length = 128)
	year = models.CharField(max_length = 1)

	def __str__(self):
		return self.userName

class CodeChef(models.Model):
	userId = models.ForeignKey(UsarData)
	userHandle = models.CharField(max_length = 128)
	problemLink = models.URLField()
	problemTitle = models.CharField(max_length = 128)
	success = models.BooleanField()
	
	def __str__(self):
		return self.problemTitle


class SPOJ(models.Model):
	userId = models.ForeignKey(UsarData)
	userHandle = models.CharField(max_length = 128)
	problemLink = models.URLField()
	problemTitle = models.CharField(max_length = 128)
	success = models.BooleanField()
	
	def __str__(self):
		return self.problemTitle

class CodeForces(models.Model):
	userId = models.ForeignKey(UsarData)
	userHandle = models.CharField(max_length = 128)
	problemLink = models.URLField()
	problemTitle = models.CharField(max_length = 128)
	success = models.BooleanField()
	
	def __str__(self):
		return self.problemTitle

class UserHandler(models.Model):
    userId= models.CharField(max_length = 40)
    codechefHandel= models.CharField(max_length = 40)
    spojHandel= models.CharField(max_length = 40)
    codeforcesHandel= models.CharField(max_length = 40)
    codechefRating= models.IntegerField
    spojRating= models.IntegerField
    codeforcesRating= models.IntegerField
    def __str__(self):
        return self.userId


class Questions(models.Model):
    problemId=models.IntegerField(unique=True)
    problemName=models.CharField(max_length = 40)
    link=models.UrlField()
    tag1=models.CharField(max_length = 40)
    tag2=models.CharField(max_length = 40)
    tag3=models.CharField(max_length = 40)
    tag4=models.CharField(max_length = 40)
    tag5=models.CharField(max_length = 40)

    def __str__(self):
        return self.problemName

