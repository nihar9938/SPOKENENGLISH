from django import forms
from . models import UserData

class AddUser_Form(forms.ModelForm):
    class Meta:
        model = UserData
        fields = '__all__'