from django.db import models
from account.models import MyUser
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	question=models.CharField(max_length=1000,default='')
	created_on=models.DateTimeField(auto_now_add=True)
	created_by=models.ForeignKey(MyUser,related_name='question_created')
	def __str__(self):
		return self.question
class Choice(models.Model):
	choice_for=models.ForeignKey(Question,related_name='choices_created')
	choice_text=models.CharField(max_length=200,blank=False)
	correct=models.BooleanField()
	created_by=models.ForeignKey(MyUser,related_name='choices_created_for')	
class Quiz(models.Model)		:
	users=models.ManyToManyField(MyUser,through='Test')
	created_on=models.DateTimeField(auto_now=True)
	ques_1=models.ForeignKey(Question,related_name='first_ques')
	ques_2=models.ForeignKey(Question,related_name='sec_ques')
	ques_3=models.ForeignKey(Question,related_name='third_ques')
	ques_4=models.ForeignKey(Question,related_name='fourth_ques')
	ques_5=models.ForeignKey(Question,related_name='fifth_ques')
	ques_6=models.ForeignKey(Question,related_name='sixth_ques')
	ques_7=models.ForeignKey(Question,related_name='seventh_ques')
	ques_8=models.ForeignKey(Question,related_name='eigth_ques')
	ques_9=models.ForeignKey(Question,related_name='ninth_ques')
	ques_10=models.ForeignKey(Question,related_name='tenth_ques')

class Test(models.Model):
	user=models.ForeignKey(MyUser,related_name='test_user')
	quiz=models.ForeignKey(Quiz,related_name='test_quiz')
	marks_scored=models.IntegerField(null=True)
	
