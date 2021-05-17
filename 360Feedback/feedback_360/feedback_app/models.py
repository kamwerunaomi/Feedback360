from django.db import models
from django.db import connections
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Department(models.Model):
	dept_id=models.IntegerField()
	dept_name=models.CharField(max_length=100)

# class User(AbstractUser):
# 	icon=models.ImageField()
# 	dept_id=models.ForeignKey(Department, on_delete=models.SET_NULL,to_field='id',null = True)
# 	#reviewee=models.array
# 	#reviewer=models.array
# 	#request=models.array



class Notifications(models.Model):
	notf_id=models.IntegerField()
	#senders_id=models.ForeignKey(User, on_delete=models.SET_NULL,to_field='id',null = True)
	receivers_id=models.ForeignKey(User, on_delete=models.SET_NULL,to_field='id',null = True)
	message=models.TextField()
	time=models.TimeField(auto_now_add=True)

class Category(models.Model):
	category_id=models.IntegerField()
	category_name=models.CharField(max_length=100)


class Questions(models.Model):
	que_id=models.IntegerField()
	category_id=models.ForeignKey(Category, on_delete=models.SET_NULL,to_field='id',null = True)
	#questions=models.array

class Answers(models.Model):
	ans_id=models.IntegerField()
	user_id=models.ForeignKey(User, on_delete=models.SET_NULL,to_field='id',null = True)
	que_id=models.ForeignKey(Questions, on_delete=models.SET_NULL,to_field='id',null = True)
	option_value=models.IntegerField()
	category_id=models.ForeignKey(Category, on_delete=models.SET_NULL,to_field='id',null = True)
	#reviewee_id=reading from array

class Average(models.Model):
	avr_id=models.IntegerField()
	#reviewee_id=reading from array
	#reviewer_id=
	#category names

class Report(models.Model):
	report_id=models.IntegerField()
	#reviewee id
	#category names



