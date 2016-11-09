from django import forms
from .models import Question
from .models import Choice
import random

class QuestionForm(forms.Form):
	question=forms.CharField(max_length=1000)
	choice1=forms.CharField(max_length=200)
	choice2=forms.CharField(max_length=200)
	choice3=forms.CharField(max_length=200)
	choice4=forms.CharField(max_length=200)
	correct_choice=forms.CharField(max_length=200)

	def clean(self):
		cleaned_data = super(QuestionForm, self).clean()
		correct_choice=cleaned_data.get("correct_choice")
		choice1=cleaned_data.get("choice1")
		choice2=cleaned_data.get("choice2")
		choice3=cleaned_data.get("choice3")
		choice4=cleaned_data.get("choice4")
		if(correct_choice !=choice1 and correct_choice!=choice2 and correct_choice!=choice3 and correct_choice!=choice4):
			raise forms.ValidationError(
				"correct choice must be equal to one of the above choices")
class PracticeForm(forms.Form)			:
	choices_given=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	def __init__(self,*args,**kwargs):
		id=kwargs.pop('id')
		super(PracticeForm,self).__init__(*args,**kwargs)
		ques_obj=Question.objects.get(pk=id)
		choice_list=[]
		choices=ques_obj.choices_created.all()
		choices=list(choices)
		while(len(choices)>0):
			x=random.choice(choices)
			y=(x.pk,x.choice_text)
			choice_list.append(y)
			choices.remove(x)
		self.fields['choices_given'].label=ques_obj.question	
		self.fields['choices_given'].choices=choice_list
class QuizForm(forms.Form)		:
	question_id_1=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_1=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	question_id_2=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_2=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	question_id_3=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_3=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	question_id_4=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_4=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	question_id_5=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_5=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	question_id_6=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_6=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	question_id_7=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_7=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	question_id_8=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_8=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	question_id_9=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_9=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	question_id_10=forms.IntegerField(widget=forms.HiddenInput())
	choices_given_10=forms.ChoiceField(widget=forms.RadioSelect(),required=False)
	def __init__(self,*args,**kwargs):
		ques_list=kwargs.pop('ques_list')
		super(QuizForm,self).__init__(*args,**kwargs)
		count=1
		while(count<=10):
			ques_obj=ques_list[count-1]
			choice_list=[]
			choices=ques_obj.choices_created.all()
			choices=list(choices)
			while(len(choices)>0):
				x=random.choice(choices)
				y=(x.pk,x.choice_text)
				choice_list.append(y)
				choices.remove(x)	
			r="Q%s"	%count
			r=r+".    "+ques_obj.question
			self.fields['question_id_%s'% count].initial=ques_obj.pk
			self.fields['choices_given_%s'% count].label=r
			self.fields['choices_given_%s'% count].choices=choice_list
			count=count+1	













    	









		
