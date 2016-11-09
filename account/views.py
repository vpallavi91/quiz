from django.shortcuts import render,get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from .forms import LoginForm,SignUpForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import create_otp,get_valid_OTP,UserOTP,MyUser
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .forms import forgetpasswordform,changepasswordform,resetform,EditForm
from .models import create_otp,MyUser,UserOTP
from django.http import HttpResponse


# Create your views here.
@require_http_methods(['GET','POST'])
def base(request):
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id':request.user.id}));
	else:
		return render(request,'common/base1.html');

@require_http_methods(['GET','POST'])
def login(request):
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id':request.user.id}));
	if request.method=='GET':
		l=LoginForm()
	else:
		l=LoginForm(request.POST)
		if l.is_valid():
			user = l.authenticated_user
			auth_login(request, user)
			return redirect(reverse('home', kwargs={'id': user.id}));
	return render(request,'account/login.html',{'l':l});


@require_GET
@login_required
def home(request, id):
	context={}
	return render(request,'account/loggedin.html',context)
def logout(request):
    auth_logout(request)
    return redirect(reverse('base'));


def signup(request):
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id':request.user.id}));
	if request.method=='GET':
		f=SignUpForm()
		return render(request,'account/signup.html',{'f':f})
	else:
		f=SignUpForm(request.POST,request.FILES)
		if not f.is_valid():
			return render(request,'account/signup.html',{'f':f})
		else:
			user = f.save(commit = False)
			user.set_password(f.cleaned_data['password'])
			user.is_active = False
			user.save()
			otp=create_otp(user=user,purpose='AA')
			email_body_context = { 'u' : user, 'otp' : otp}
			body = loader.render_to_string('account/email/activate_account.txt', email_body_context)
			message = EmailMultiAlternatives("Activate Account", body, settings.EMAIL_HOST_USER, [f.cleaned_data.get('email','')])
			#message.attach_alternative(html_body, 'text/html')
			message.send()
			return render(request, 'account/activate_account_sent.html', {'u': user});
@require_GET
def activate_account(request,id = None, otp = None):
	if request.user.is_authenticated():
		return redirect('home',{'id':request.user.id})
	user=get_object_or_404(MyUser,id=id)
	if user and not UserOTP.objects.filter(user=user,otp=otp,purpose='AA').exists():
		raise Http404('invalid OTP')
	otpobj=UserOTP.objects.get(user=user,otp=otp,purpose='AA')
	otpobj.delete()
	user.is_active=True
	user.save()
	return render(request,'account/login.html',{'u':user})
def forgetpassword(request):
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id':request.user.id}))
	if (request.method=='GET'):
		f=forgetpasswordform()
		return render(request,'account/forget.html',{'f':f})
	if(request.method=='POST')	:
		f=forgetpasswordform(request.POST)
		if not f.is_valid():
			return render(request,'account/forget.html',{'f':f})
		else:
			username=f.cleaned_data['username']
			user=MyUser.objects.get(username=username)
			otp=create_otp(user,'FP')
			email_body_context = { 'u' : user, 'otp' : otp}
			body = loader.render_to_string('account/forgot_password.txt', email_body_context)
			message = EmailMultiAlternatives("Reset Password", body, settings.EMAIL_HOST_USER, [user.email])
			message.send()
			return render(request,'account/emailsent.html',{'u':user}) 	
def reset(request,id=None,otp=None):
	if (request.method=='GET'):
		if request.user.is_authenticated():
			return redirect('home',{'id':id})
		user=MyUser.objects.get(id=id)	
		if 	not user :
			raise Http404
		if  UserOTP.objects.filter(user=user,otp=otp).exists():

			userobject=UserOTP.objects.get(user=user,otp=otp)
			userobject.delete()
			f=resetform()
			return render(request,'account/reset.html',{'f':f,'uid':id,'otp':otp})
		else:
			raise Http404
	if(request.method=='POST')		:
		if request.user.is_authenticated():
			return redirect('home',{'id':id})
		f=resetform(request.POST)
		if not f.is_valid():
			user=MyUser.objects.get(id=id)
			return render(request,'account/reset.html',{'f':f,'uid':id,'otp':otp})
		else:
			user=MyUser.objects.get(id=id)
		if not user:
			raise Http404
		else:
			password=f.cleaned_data['newpassword']
			user.set_password(password)
			user.save()
			return render(request,'account/passwordchanged.html',{'u':user})
@require_http_methods(['GET','POST'])	
@login_required
def change(request):
	if (request.method=='GET'):
		f=changepasswordform()
		return render(request,'account/changepassword.html',{'f':f})

	if(request.method=='POST')	:
		f=changepasswordform(request.POST,user=request.user)
		if not f.is_valid():
			return render(request,'account/changepassword.html',{'f':f})
		else:
			user=request.user
			user.set_password(f.cleaned_data['new_password'])
			user.save()
			auth_logout(request)
			return render(request,'account/passwordchanged.html')	




@require_http_methods(['GET','POST'])
@login_required
def edit_profile(request,id=None):
	profile_obj=get_object_or_404(MyUser,id=id)
	print(request.user)
	if profile_obj.username!=request.user.username:
		raise Http404()
	if request.method=='GET':
		q=EditForm(instance=profile_obj)
	else:
		q=EditForm(request.POST,request.FILES,instance=profile_obj)
		if q.is_valid():
			profile_obj=q.save()
			return redirect(reverse('home',kwargs={'id':request.user.id}))
	return render(request, 'account/edit.html',{'q':q})	


@login_required
def view_profile(request,id=None):
	user=get_object_or_404(MyUser,id=id)
	if(request.user!=user):
		raise Http404();
	else:
		context={'user':user}
		return render(request, 'account/profile.html',context)






