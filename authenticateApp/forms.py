from django.forms import ModelForm
from django import forms
from facultyManagementApp.models import User
from facultyManagementApp.globals import departmentList, userLevelList

class RegisterForm(ModelForm):

    userLevel = forms.ChoiceField(label="User Type", choices=userLevelList, widget=forms.Select(attrs={"class":"form-select form-select", "aria-label":".form-select-lg example"}),
        error_messages={'required': 'User Type is required'})
    department = forms.ChoiceField(label="Department", choices=departmentList, widget=forms.Select(attrs={"class":"form-select form-select", "aria-label":".form-select-lg example"}),
        error_messages={'required': 'Department is required'})
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control", "autofocus":"autofocus"}), 
            error_messages={'required': 'Email is required', 'invalid' : 'Your email is invalid'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "required":"required"}),
            error_messages={'required': 'Password is required'})
    firstName = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "autofocus":"autofocus"}) ,
            error_messages={'required': 'First name is required'})
    lastName = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "required":"required", "autofocus":"autofocus"}),
            error_messages={'required': 'Last name is required'})
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "required":"required", "autofocus":"autofocus"}),
            error_messages={'required': 'Username is required'})


    class Meta:
        model = User
        fields = ['userLevel','department', 'firstName', 'lastName','username','email', 'password']

# class RegisterForm(forms.Form):
#     email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"1"}))
#     password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"1"}))
#     firstName = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"1"}))
#     lastName = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"1"}))
#     username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"1"}))
#     userLevelList = (
#         ('1','Faculty'),
#         ('2','Department Head'),
#         ('3','Research Coordinator'),
#         ('4','Extension Coordinator'),
#     )
#     userLevel = forms.ChoiceField(label="Role", choices=userLevelList, widget=forms.Select(attrs={"class":"1"}))
#     class Meta:
#         model = User