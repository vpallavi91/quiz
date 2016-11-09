from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint

# Create your models here.
class MyUser(AbstractUser):
	phone=models.CharField(max_length=10,null=True)
	profile_pic=models.ImageField(upload_to='profile_pics/',null=True,blank=True)


def create_otp(user=None,purpose=None):
	if not user:
		raise ValueError('Invalid Arguments')
	choices=[]
	for data,verbose in UserOTP.Purpose_Choices:
		choices.append(data)
	if not purpose in choices:
		raise ValueError('Invalid Arguments')
	if UserOTP.objects.filter(user=user,purpose=purpose).exists():
		old_otp=UserOTP.objects.filter(user=user,purpose=purpose)
		old_otp.delete()
	otp=randint(1000,9999)
	otp_object = UserOTP.objects.create(user = user, purpose = purpose, otp = otp)
	return otp
def get_valid_OTP(user=None,purpose=None,otp=None):
	if not user:
		raise ValueError('Invalid Arguments')
	choices=[]
	for data,verbose in UserOTP.Purpose_Choices:
		choices.append(data)
	if not purpose in choices:
		raise ValueError('Invalid Arguments')
	try:
		otp_object = UserOTP.objects.get(user = user, purpose=purpose, otp=otp)
		return otp_object
	except UserOTP.DoesNotExist:
		return None



class UserOTP(models.Model):
	Purpose_Choices=(
		('FP','Forgot Password'),
		('AA','Activation Account'),
		('CP','Change Password'));
	user=models.ForeignKey(MyUser)
	otp=models.CharField(max_length=4)
	purpose=models.CharField(max_length=2,choices=Purpose_Choices)
	created_on=models.DateTimeField(auto_now_add=True)
	class Meta:
		unique_together=['user','purpose']

