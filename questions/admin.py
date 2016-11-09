from django.contrib import admin
from .models import Question,Choice

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display=['question','created_by','created_on']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
	list_display=['choice_for','choice_text','correct']
