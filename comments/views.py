from django.shortcuts import render,get_object_or_404,redirect
from questions.models import Question
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST,require_http_methods


# Create your views here.
#id stands for question id,id1 stands for comment id
@require_http_methods(['GET','POST'])
@login_required
def submit_comment(request,id=None,id1=None):
	ques_obj=get_object_or_404(Question,id=id)
	if request.method=='GET':
		q=CommentForm()
		return render(request,'comment/add_comment.html',{'q':q})
	else if request.method=='POST':
		q=CommentForm(request.POST)
		if q.is_valid():
			comment_obj=Comment.objects.create(text=q.cleaned_data.get('text'),for_ques=ques_obj,created_by=)




