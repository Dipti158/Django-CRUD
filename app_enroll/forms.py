
from django import forms
from app_enroll.models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields = ['name','email','password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value=True,attrs={'class':'form-control'}) # render_value to show password while update form open
        } 