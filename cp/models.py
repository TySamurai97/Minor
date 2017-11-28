from django.db import models

class UserData(models.Model):
	userName = models.CharField(max_length = 128)
	spojHandle = models.CharField(max_length = 40,null=True)
	codeforcesHandle = models.CharField(max_length = 40,null=True)
	codeforcesRating = models.IntegerField(null=True)
	
	def __str__(self):
		return self.userName

class SPOJ(models.Model):
	userdata = models.ForeignKey(UserData)
	userHandle = models.CharField(max_length = 128,null=True)
	problemLink = models.URLField(null=True)
	problemTitle = models.CharField(max_length = 128,null=True)
	success = models.NullBooleanField()
	
	def __str__(self):
		return self.problemTitle

class CodeForces(models.Model):
	userdata = models.ForeignKey(UserData)
	userHandle = models.CharField(max_length = 128,null=True)
	problemLink = models.URLField(null=True)
	problemTitle = models.CharField(max_length = 128,null=True)
	success = models.NullBooleanField()

	
	def __str__(self):
		return self.problemTitle

class Problems(models.Model):
	problemTitle = models.CharField(max_length = 128)
	tag = models.CharField(max_length = 128)

	def __str__(self):
		return self.problemTitle