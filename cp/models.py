from django.db import models

# Create your models here.
class UserData(models.Model):
	userName = models.CharField(max_length = 128)
	passWord = models.CharField(max_length = 128)
	userEmail = models.URLField()
	mobileNo = models.CharField(max_length = 128)
	Gender = models.CharField(max_length = 1)
	collageOrCompany = models.CharField(max_length = 128)
	year = models.CharField(max_length = 1)

	def __str__(self):
		return self.userName

class CodeChef(models.Model):
	userdata = models.ForeignKey(UserData)
	userHandle = models.CharField(max_length = 128)
	problemLink = models.URLField()
	problemTitle = models.CharField(max_length = 128)
	success = models.BooleanField()

	def __str__(self):
		return self.problemTitle

class SPOJ(models.Model):
	userdata = models.ForeignKey(UserData)
	userHandle = models.CharField(max_length = 128)
	problemLink = models.URLField()
	problemTitle = models.CharField(max_length = 128)
	success = models.BooleanField()
	
	def __str__(self):
		return self.problemTitle

class CodeForces(models.Model):
	userdata = models.ForeignKey(UserData)
	userHandle = models.CharField(max_length = 128)
	problemLink = models.URLField()
	problemTitle = models.CharField(max_length = 128)
	success = models.BooleanField()
	
	def __str__(self):
		return self.problemTitle

class UserHandle(models.Model):
    codechefHandle = models.CharField(max_length = 40)
    spojHandle = models.CharField(max_length = 40)
    codeforcesHandle = models.CharField(max_length = 40)
    codechefRating = models.IntegerField
    spojRating = models.IntegerField
    codeforcesRating = models.IntegerField
    def __str__(self):
        return self.userId

class Questions(models.Model):
    problemName = models.CharField(max_length = 40)
    link = models.URLField()
    tag1 = models.CharField(max_length = 40)
    tag2 = models.CharField(max_length = 40)
    tag3 = models.CharField(max_length = 40)
    tag4 = models.CharField(max_length = 40)
    tag5 = models.CharField(max_length = 40)

    def __str__(self):
        return self.problemName
