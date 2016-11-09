from django import forms
from .models import MyUser
from django.contrib.auth import authenticate
class LoginForm(forms.Form):
	username=forms.CharField(max_length=20)
	password=forms.CharField(widget = forms.PasswordInput)
	def __init__(self, *args, **kwargs):
		self.authenticated_user = None;
		super(LoginForm, self).__init__(*args, **kwargs)
	def clean_username(self):
		data_username=self.cleaned_data.get('username','')
		if MyUser.objects.filter(username=data_username).count()!=1:
			raise forms.ValidationError('Invalid Username')
		return data_username
	def clean(self):
		data_username=self.cleaned_data.get('username','')
		data_password=self.cleaned_data.get('password','')
		user=authenticate(username=data_username,password=data_password)
		if data_username and data_password and not user:
			raise forms.ValidationError('Username/Password Does Not Match')
		if user and (user.is_active==False):
			raise forms.ValidationError('Inactive User')
		self.authenticated_user = user
		return self.cleaned_data;

class SignUpForm(forms.ModelForm):
	password=forms.CharField(max_length=30,widget=forms.PasswordInput)
	confirm_password=forms.CharField(max_length=30,widget=forms.PasswordInput)
	def clean_email(self):
		data_email=self.cleaned_data.get('email','')
		if not data_email:
			raise forms.ValidationError('Invalid Email')
		return data_email
	def clean_confirm_password(self):
		data_password=self.cleaned_data.get('password','')
		data_confirm_password=self.cleaned_data.get('confirm_password','')
		if data_password!=data_confirm_password:
			raise forms.ValidationError('Password Doesnt match')
		return data_confirm_password
	class Meta:
		model=MyUser
		fields=['username','email','phone','profile_pic']
class forgetpasswordform(forms.Form):
	username=forms.CharField(max_length=100)
	def clean_username(self):
		username=self.cleaned_data.get('username','')
		if username and MyUser.objects.filter(username=username).count()!=1	:
			raise forms.ValidationError('Invalid username')
		return self.cleaned_data['username']
class resetform(forms.Form)		:
	newpassword=forms.CharField(widget=forms.PasswordInput)
	confirmpassword=forms.CharField(widget=forms.PasswordInput) 
	def clean(self):
		if not (self.cleaned_data['newpassword']==self.cleaned_data['confirmpassword']):
			raise forms.ValidationError('new password and confirm password doesnot match')
		else:
			return self.cleaned_data
class changepasswordform(forms.Form)		:
	current_password=forms.CharField(widget=forms.PasswordInput)
	new_password=forms.CharField(widget=forms.PasswordInput)
	confirm_password=forms.CharField(widget=forms.PasswordInput)
	def __init__(self,*args,**kwargs):
		self.user=kwargs.pop('user','')
		super(changepasswordform,self).__init__(*args,**kwargs)
	def clean_current_password(self):
		username=self.user.username
		password=self.cleaned_data['current_password']
		tuser=authenticate(username=username,password=password)
		if not tuser:
			raise forms.ValidationError('Invalid Password')
		return self.cleaned_data	

	def clean(self)	:
		passwd=self.cleaned_data.get('password','')
		confirmpasswd=self.cleaned_data.get('confirmpassword','')
		if (passwd==confirmpasswd):
			return self.cleaned_data
		raise forms.ValidationError('passwords doenot match')	



class EditForm(forms.ModelForm):
	class Meta:
		model=MyUser
		fields=['username','email','phone','profile_pic']				