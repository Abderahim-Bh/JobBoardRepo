from django import forms
from . models import Candidates,JobModel


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = [ 
            'name',
            'email',
            'website',
            'cv',
            'coverLetter'
        ]

class JobModelForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = '__all__'
        exclude = ('slug', 'user')