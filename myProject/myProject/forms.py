
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from myApp.models import customUser, addJobModel,jobApplyModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = customUser
        fields = UserCreationForm.Meta.fields + ('city', 'user_type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            self.fields[field_name].help_text = None

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = customUser  
        fields = ['username', 'password']

class addJobForm(forms.ModelForm):
    class Meta:
        model = addJobModel
        fields = ['Job_Title', 'Job_Description', 'Job_Requirements']
        labels = {
            'Job_Title': 'Enter Your Job Title',
            'Job_Description': 'Enter Your Job Description',
            'Job_Requirements': 'Enter Your Job Requirements',
        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = jobApplyModel
        fields = ['skills', 'resume']
        labels = {
            'applicant_name': 'Your Name',
            'applicant_email': 'Your Email',
            'cover_letter': 'Cover Letter',
        }
class MaximumNumberForm(forms.Form):
    a = forms.IntegerField(label='Number A')
    b = forms.IntegerField(label='Number B')
    c = forms.IntegerField(label='Number C')