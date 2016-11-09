from django.db import models
from account.models import MyUser
from questions.models import Question

# Create your models here.
class Quiz(models.Model):
	users=models.ManyToManyField(MyUser,through='Test')
	questions=models.ManyToManyField(Question,through='Test')

class Test(models.Model):
	user=models.ForeignKey(MyUser)
	quiz=models.ForeignKey(Quiz)
	marks_scored=models.IntegerField(null=True)
	ques_1=models.ForeignKey(Question)
	ques_2=models.ForeignKey(Question)
	ques_3=models.ForeignKey(Question)
	ques_4=models.ForeignKey(Question)
	ques_5=models.ForeignKey(Question)
	ques_6=models.ForeignKey(Question)
	ques_7=models.ForeignKey(Question)
	ques_8=models.ForeignKey(Question)
	ques_9=models.ForeignKey(Question)
	ques_10=models.ForeignKey(Question)
