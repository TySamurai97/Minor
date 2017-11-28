from django.db import models

class UserData(models.Model):
	userName = models.CharField(max_length = 128)
	spojHandle = models.CharField(max_length = 40,null=True)
	codeforcesHandle = models.CharField(max_length = 40,null=True)
	codeforcesRating = models.CharField(max_length = 40,null=True)
	spojRating = models.CharField(max_length = 40,null=True)

	
	
	def __str__(self):
		return self.userName

class UserStats(models.Model):
	userData = models.ForeignKey(UserData)
	userName = models.CharField(max_length = 128)

	implementation = models.IntegerField(null=True)
	binarySearch = models.IntegerField(null=True)
	dp= models.IntegerField(null=True)
	gameTheory = models.IntegerField(null=True)
	graphs = models.IntegerField(null=True)
	greedy = models.IntegerField(null=True)
	hashing = models.IntegerField(null=True)
	math = models.IntegerField(null=True)
	string = models.IntegerField(null=True)
	dataStructures = models.IntegerField(null=True)

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
	problemTitle = models.CharField(max_length = 128,null = True)
	tag = models.CharField(max_length = 128,null = True)

	def __str__(self):
		return self.problemTitle