from django import forms
############
from blog.models import User
############
from django.core import validators
## Django l5 Authentication
from django.contrib.auth.models import User
from blog.models import UserProfileInfo



# self Validtion
def check_ali(value):
    if 'ali' in value:
        raise forms.ValidationError('Ali is in form es ist Verboten')


# Forms

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields="__all__"



#### USER FORM

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model= UserProfileInfo
        fields=('portfolio_site','portfolio_pic')



class add_text(forms.Form):
    title = forms.CharField(validators=[validators.MaxLengthValidator(2,'Sie duerfen nur zwei nomen nuntzen')])
    text  = forms.CharField(validators=[check_ali],widget=forms.Textarea)
    file = forms.FileField()
def clean(self):
    all_clean_data=super().clean()

class registration(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.PasswordInput
    vpassword=forms.PasswordInput
    email = forms.EmailField()
    vemail = forms.EmailField()
class user_login(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
