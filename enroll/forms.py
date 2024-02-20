from django.core import validators
from django import forms 
from .models import User 


def start_with_s(value):
    if value[0]!='s':
        raise forms.ValidationError("name should start with S")
    
class UserForm(forms.ModelForm):
    #name= forms.CharField(validators=[start_with_s])
    #password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User 
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'})
        }