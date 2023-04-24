from django import forms
from . models import Candidates


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = [ 
            'job',
            'name',
            'email',
            'website',
            'cv',
            'coverLetter'
        ]
