from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User,excel_file

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_hod', 'is_staff')
class ExcelUpload(forms.ModelForm):
    class Meta:
        model=excel_file
        
        fields=['S_No','RollNo','Name','GradeR','PointsR','CreditsR','Resc','GradeW','PointsW','CreditsW','web_tech','GradeD','PointsD','CreditsD','Dis_sys','GradeD1','PointsD1','CreditsD1','Design','GradeM','PointsM','CreditsM','Mefa','GradeI','PointsI','CreditsI','Info','Gradew1','Pointsw1','Creditsw1','wlab','sgpa','Tot_cr','pass1','bclg']