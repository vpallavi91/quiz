from django.conf.urls import url
from .views import home,logout,signup,activate_account,login,edit_profile,view_profile
from . import views


urlpatterns = [
url(r'^(?P<id>\d+)/home/$',home,name='home'),
url(r'^logout/$',logout,name='logout'),
url(r'^activate/(?P<id>\d+)/(?P<otp>\d{4})/$', activate_account, name='activate-account'),
url(r'^signup/$',signup,name='signup'),
url(r'forgetpassword/',views.forgetpassword,name='forget'),
url(r'reset/(?P<id>[0-9]+)/(?P<otp>[0-9]+)/',views.reset,name='reset'),
url(r'change/',views.change,name='change'),
url(r'^login/$', login, name = 'login'),
url(r'^(?P<id>\d+)/edit/$',edit_profile,name='edit-profile'),
url(r'^(?P<id>\d+)/user-profile/$',view_profile,name='view-profile'),

]