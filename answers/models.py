from django.db import models
from account.models import MyUser
from questions.models import Choice
from questions.models import Question

# Create your models here.
class Answer(models.Model):
	created_by=models.ForeignKey(MyUser,related_name='answer_created')
	answer=models.ForeignKey(Choice,related_name='ans_selected')
	answer_to=models.ForeignKey(Question,related_name='answer_given')
