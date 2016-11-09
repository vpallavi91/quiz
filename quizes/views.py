from questions.models import Question,Choice
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from account.models import MyUser
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404, JsonResponse, HttpResponse
import random
from .forms import QuizForm
from .models import Test,Quiz

# Create your views here.
@require_http_methods(['GET','POST'])
@login_required
def take_quiz(request,id=None):
	if(request.method=='GET'):
		if(id==None):
			questions=Question.objects.all()
			questions=list(questions)
			if(len(questions<10)):
				raise Http404()
			user=request.user
			count=0
			ques=[]
			while(count<10):
				x=random.choice(questions)
				ques.append(x)
				questions.remove(x)
				count=count+1
            quiz=Quiz.objects.create()
			test=Test.objects.create(user=user,quiz=quiz,ques_1=ques[0],ques_2=ques[1],ques_3=ques[2],ques_4=ques[3],ques_5=ques[4],ques_6=ques[5],ques_7=ques[6],ques_8=ques[7],ques_9=ques[8],ques_10=ques[9])
		else:
			test=Test.objects.get(id)
		q=QuizForm(test.id)
		return render(request,'quizes/quiz.html',{'test_id':test.id,'q':q})		

			



