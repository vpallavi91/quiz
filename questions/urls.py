from django.conf.urls import url, include
from questions.views import add_question,edit_question,practice,take_quiz,search,results,result,check_quiz
from account.views import home
urlpatterns = [
url(r'^add/$',add_question,name='add-question'),
url(r'^(?P<id>\d+)/edit/$',edit_question,name='edit-question'),
url(r'^(?P<id>\d+)/home/$',home,name='back-home'),
url(r'^practice/$',practice,name='prac'),
url(r'^(?P<id>\d+)/practice/$',practice,name='prac-ques'),
url(r'^quiz/$',take_quiz,name='new-quiz'),
url(r'^(?P<id>\d+)/quiz/$',take_quiz,name='prac-quiz'),
url(r'^search/$',search,name='search-question'),
url(r'(?P<id>\d+)/results/$',results,name='results'),
url(r'^(?P<id>\d+)/check_quiz/$',check_quiz,name='check-quiz'),
url(r'^(?P<id>\d+)/result/$',result,name='result')
]