from django import forms
from poll.models import Question


class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}))

    class Meta:
        model = Question
        fields = ('question_text',)