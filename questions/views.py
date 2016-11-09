from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import QuestionForm,PracticeForm,QuizForm
from .models import Question,Choice,Quiz,Test
from django.core.urlresolvers import reverse
from account.models import MyUser
from random import randint
import random

# Create your views here.
@require_http_methods(['GET','POST'])
@login_required
def add_question(request):
	if request.method=='GET':
		q=QuestionForm()
		return render(request,'question/add.html',{'q':q})
	else:
		q=QuestionForm(request.POST)		
		if q.is_valid():
			ques_obj=Question.objects.create(question=q.cleaned_data.get('question'),created_by=request.user)
			correct_choice=Choice.objects.create(choice_for=ques_obj,choice_text=q.cleaned_data.get('correct_choice'),correct=True,created_by=request.user)
			correct_text=q.cleaned_data.get('correct_choice')
			choice1_text=q.cleaned_data.get('choice1')
			if(choice1_text!=correct_text):
				choice1=Choice.objects.create(choice_for=ques_obj,choice_text=choice1_text,correct=False,created_by=request.user)
			choice2_text=q.cleaned_data.get('choice2')	
			if(choice2_text!=correct_text):
				choice2=Choice.objects.create(choice_for=ques_obj,choice_text=choice2_text,correct=False,created_by=request.user)
			choice3_text=q.cleaned_data.get('choice3')	
			if(choice3_text!=correct_text):
				choice3=Choice.objects.create(choice_for=ques_obj,choice_text=choice3_text,correct=False,created_by=request.user)	
			choice4_text=q.cleaned_data.get('choice4')	
			if(choice4_text!=correct_text):
				choice1=Choice.objects.create(choice_for=ques_obj,choice_text=choice4_text,correct=False,created_by=request.user)	



			return redirect(reverse('back-home',kwargs={'id':request.user.id}))
		else:
			return render(request,'question/add.html',{'q':q})

@require_http_methods(['GET','POST'])
@login_required
def edit_question(request,id=None):
	ques_obj=get_object_or_404(Question,id=id)
	if  ques_obj.created_by!=request.user:
		raise Http404()
	if request.method=='GET':
		choices=ques_obj.choices_created.all()
		question=ques_obj.question
		for ch1 in choices:
			if(ch1.correct==True):
				correct_choice=ch1.choice_text
		choice1=choices[0].choice_text
		choice2=choices[1].choice_text
		choice3=choices[2].choice_text
		choice4=choices[3].choice_text
		q=QuestionForm(initial={'question':question,'correct_choice':correct_choice,'choice1':choice1,'choice2':choice2,'choice3':choice3,'choice4':choice4})

	else:
		q=QuestionForm(request.POST)
		if q.is_valid():
			ques_obj.question=q.cleaned_data.get('question')
			ques_obj.save()
			correct_choice=q.cleaned_data.get('correct_choice')
			choices=Choice.objects.filter(choice_for=ques_obj)
			choice1=Choice.objects.get(pk=choices[0].pk)
			choice1.choice_text=q.cleaned_data.get('choice1')
			if choice1.choice_text==correct_choice:
				choice1.correct=True
			else:
				choice1.correct=False	
			choice1.save()
			choice2=Choice.objects.get(pk=choices[1].pk)
			choice2.choice_text=q.cleaned_data.get('choice2')
			if choice2.choice_text==correct_choice:
				choice2.correct=True
			else:
				choice2.correct=False	
			choice2.save()
			choice3=Choice.objects.get(pk=choices[2].pk)
			choice3.choice_text=q.cleaned_data.get('choice3')
			if choice3.choice_text==correct_choice:
				choice3.correct=True
			else:
				choice3.correct=False
				
			choice3.save()
			choice4=Choice.objects.get(pk=choices[3].pk)
			choice4.choice_text=q.cleaned_data.get('choice4')
			if choice4.choice_text==correct_choice:
				choice4.correct=True
			else:
				choice4.correct=False	
			choice4.save()



			return redirect(reverse('back-home',kwargs={'id':request.user.id}))
	context = { 'q' : q, 'q_id': ques_obj.id }
	return render(request, 'question/edit.html', context)
@require_http_methods(['GET','POST'])
@login_required
def practice(request,id=None):
	if request.method=='GET':
		if(id==None):
			ques_list=Question.objects.all()
			ques_list=list(ques_list)
			if(len(ques_list)==0):
				return render(request,'question/end.html')
			return render(request,'question/practice_list.html',{'ques_list':ques_list})	
		else:
			ques_obj=get_object_or_404(Question,pk=id)
		p=PracticeForm(id=id)
		context={'p':p,'q_id':ques_obj.id,'q_text':ques_obj.question}
		return render(request,'question/practice.html',context)
	if request.method=='POST':
		if(id==None):
			raise Http404()
		else:
			ques_obj=Question.objects.get(pk=id)
			p=PracticeForm(request.POST,id=id)
			if (p.is_valid()):
				choices=ques_obj.choices_created.all()
				k=False
				for x in choices:
					if(x.correct==True):
						correct=x.pk
				correct=Choice.objects.get(pk=correct)
				return JsonResponse({'correct':correct.choice_text})
			else:
				context={'p':p,'q_id':ques_obj.id,'q_text':ques_obj.question}
				return render(request,'question/practice.html',context)
@require_http_methods(['GET','POST'])
@login_required
def take_quiz(request,id=None):
	if(request.method=='GET'):
		if(id==None):
			testlist=Test.objects.filter(user=request.user)
			quizlist=Quiz.objects.all()
			quizlist2=[]
			ques_list=[]
			testlist=list(testlist)
			for g in testlist:
				quizlist2.append(g.quiz)
			t=False	
			quiz=0
			for val in quizlist:
				if(val not in quizlist2):
					t=True
					quiz=val
					ques_list.append(quiz.ques_1)
					ques_list.append(quiz.ques_2)
					ques_list.append(quiz.ques_3)
					ques_list.append(quiz.ques_4)
					ques_list.append(quiz.ques_5)
					ques_list.append(quiz.ques_6)
					ques_list.append(quiz.ques_7)
					ques_list.append(quiz.ques_8)
					ques_list.append(quiz.ques_9)
					ques_list.append(quiz.ques_10)
					break


			if(t==False):
				ques=Question.objects.all()
				ques=list(ques)
				if(len(ques)<10):
					raise Http404
				count=0
				while(count<10):
					k=random.choice(ques)
					ques_list.append(k)
					ques.remove(k)
					count=count+1
				quiz=Quiz.objects.create(ques_1=ques_list[0],ques_2=ques_list[1],ques_3=ques_list[2],ques_4=ques_list[3],ques_5=ques_list[4],ques_6=ques_list[5],ques_7=ques_list[6],ques_8=ques_list[7],ques_9=ques_list[8],ques_10=ques_list[9])	
			user=request.user
			test=Test.objects.create(user=user,quiz=quiz)
		else:
			test=get_object_or_404(Quiz,pk=id)
			test_list=Test.objects.filter(user=request.user)
			key=False
			for item in test_list:
				if(item.quiz==test):
					key=True
					break
			if(key==True)	:
				raise Http404	
			
			if(request.user!=test.user):
				raise Http404()
			ques_list=[]
			k=quiz.ques_1
			ques_list.append(k)
			k=quiz.ques_2
			ques_list.append(k)
			k=quiz.ques_3
			ques_list.append(k)
			k=quiz.ques_4
			ques_list.append(k)
			k=quiz.ques_5
			ques_list.append(k)
			k=quiz.ques_6
			ques_list.append(k)
			k=quiz.ques_7
			ques_list.append(k)
			k=quiz.ques_8
			ques_list.append(k)
			k=quiz.ques_9
			ques_list.append(k)
			k=quiz.ques_10
			ques_list.append(k)
		q=QuizForm(ques_list=ques_list)
		return render(request,'question/quiz.html',{'q':q,'test_id':test.id})
	if(request.method=='POST')	:
		if(id==None):
			raise Http404()
		test=get_object_or_404(Test,pk=id)	
		quiz=test.quiz	
		if(request.user!=test.user):
			raise Http404()
		if(test.marks_scored!=None):
			raise Http404	
		ques_list=[]
		k=quiz.ques_1
		ques_list.append(k)
		k=quiz.ques_2
		ques_list.append(k)
		k=quiz.ques_3
		ques_list.append(k)
		k=quiz.ques_4
		ques_list.append(k)
		k=quiz.ques_5
		ques_list.append(k)
		k=quiz.ques_6
		ques_list.append(k)
		k=quiz.ques_7
		ques_list.append(k)
		k=quiz.ques_8
		ques_list.append(k)
		k=quiz.ques_9
		ques_list.append(k)
		k=quiz.ques_10
		ques_list.append(k)
		q=QuizForm(request.POST,ques_list=ques_list)
		label_list=[]
		if(q.is_valid()):
			count=1
			marks=0
			while(count<=10):
				ques_obj=q.cleaned_data['question_id_%s' %count]
				ques_obj=Question.objects.get(pk=ques_obj)
				value=q.cleaned_data.get('choices_given_%s' %count)
				choices=ques_obj.choices_created.all()
				k=False
				for x in choices:
					if(x.correct==True):
						correct=x.pk
				correct=Choice.objects.get(pk=correct)
				try:
					value=Choice.objects.get(pk=value)
				except:
					value=None	
				if(correct==value)	:
					k=True
				if(k==True)	:
					marks=marks+4
					label_list.append({ques_obj.question:ques_obj.question+' '+'correct'})
				elif(value==None):
					mark=marks;
					label_list.append({ques_obj.question:ques_obj.question+' '+'not attempted'})
				else:
					marks=marks-1;
					label_list.append({ques_obj.question:ques_obj.question+' '+'wrong'})
				count=count+1
				test.marks_scored=marks
				test.save()
			return redirect(reverse('result',kwargs={'id':test.pk}));
			return render(request,'question/quiz.html',{'q':q,'test_id':test.id})


@require_GET
@login_required
def search(request):
	term=request.GET.get('term')
	questions=Question.objects.filter(question__startswith=term)[:3]	
	data=[{'question':ques.question,'id':ques.id} for ques in questions]
	return JsonResponse({'data':data})	


@login_required
def results(request,id=None):
	user=get_object_or_404(MyUser,id=id)
	if(user!=request.user):
		raise Http404();
	else:
		test_taken=Test.objects.filter(user=user)
		test_taken2=[]
		for x in test_taken:
		    if(x.marks_scored!=None):
		        test_taken2.append(x)
		context={'test_taken':test_taken2}
		return render(request,'question/result1.html',context)	
@login_required
def result(request,id)	:
	test=get_object_or_404(Test,pk=id)
	marks=test.marks_scored
	return render(request,'question/result.html',{'marks':marks,'m':'marks scored'})
@require_POST
@login_required
def check_quiz(request,id):
		test=get_object_or_404(Test,pk=id)	
		quiz=test.quiz
		if(test.marks_scored!=None):
			raise Http404
		ques_list=[]
		k=quiz.ques_1
		ques_list.append(k)
		k=quiz.ques_2
		ques_list.append(k)
		k=quiz.ques_3
		ques_list.append(k)
		k=quiz.ques_4
		ques_list.append(k)
		k=quiz.ques_5
		ques_list.append(k)
		k=quiz.ques_6
		ques_list.append(k)
		k=quiz.ques_7
		ques_list.append(k)
		k=quiz.ques_8
		ques_list.append(k)
		k=quiz.ques_9
		ques_list.append(k)
		k=quiz.ques_10
		ques_list.append(k)
		q=QuizForm(request.POST,ques_list=ques_list)
		label_list=[]
		if(q.is_valid()):
			count=1
			marks=0
			while(count<=10):
				ques_obj=q.cleaned_data['question_id_%s' %count]
				ques_obj=Question.objects.get(pk=ques_obj)
				value=q.cleaned_data.get('choices_given_%s' %count)
				choices=ques_obj.choices_created.all()
				k=False
				for x in choices:
					if(x.correct==True):
						correct=x.pk
				correct=Choice.objects.get(pk=correct)
				try:
					value=Choice.objects.get(pk=value)
				except:
					value=None	
				if(correct==value)	:
					k=True
				if(k==True)	:
					marks=marks+4
					label_list.append(correct.choice_text)
				elif(value==None):
					mark=marks;
					label_list.append(correct.choice_text)
				else:
					marks=marks-1;
					label_list.append(correct.choice_text)
				count=count+1
				test.marks_scored=marks
				test.save()
			return JsonResponse({'label_list':label_list,'result':marks})
		else:
			return JsonResponse({'errors':q.errors})








		    	
