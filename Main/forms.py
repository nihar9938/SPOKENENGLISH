from django import forms
from .models import *

class AddNews_Form(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            "title":forms.TextInput(attrs={"placeholder":"Enter news here..", "name":"title", "class":"form-control", }),
             "valid":forms.CheckboxInput(attrs={"name":"valid", "required": False})
        }


class EditNews_Form(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            "title":forms.TextInput(attrs={"placeholder":"Enter news here..", "name":"title", "class":"form-control", }),
             "valid":forms.CheckboxInput(attrs={"name":"valid", "required": False})
        }
class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'