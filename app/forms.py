from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class WebpageForm(forms.ModelForm):
    class Meta:
        model=webpage
        fields='__all__'
class AccessForm(forms.ModelForm):
    class Meta:
        model=AR
        fields='__all__'