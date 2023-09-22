from django import forms 

from .models import * 

class Signup(forms.ModelForm):
    class Meta : 
        model = Userinfo
        fields = '__all__'
        labels = {'name':'Full Name ','email':'Email ', 'address':'Address '}