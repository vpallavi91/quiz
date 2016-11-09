from django.conf.urls import url
from .views import take_quiz
urlpatterns=[url(r'^new/$',take_quiz,name='new-quiz')]