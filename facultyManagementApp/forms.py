from django.forms import ModelForm
# from .models import 
from django import forms
from .models import User, Subject, Extension, Research, Announcement
from .globals import departmentList, userLevelList

class updateProfile(ModelForm):
        firstName = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "autofocus":"autofocus"}) ,
                error_messages={'required': 'This field is required'})
        lastName = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "required":"required", "autofocus":"autofocus"}),
                error_messages={'required': 'This field is required'})
        username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "required":"required", "autofocus":"autofocus"}),
                error_messages={'required': 'This field is required'})
        email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control", "autofocus":"autofocus"}), 
                error_messages={'required': 'This field is required', 'invalid' : 'Your email is invalid'})
        department = forms.ChoiceField(label="Department", choices=departmentList, widget=forms.Select(attrs={"class":"form-select form-select", "aria-label":".form-select-lg example"}))

        class Meta:
                model = User
                fields = ['firstName', 'lastName', 'username', 'email', 'department']

class updateProfileAdmin(ModelForm):
        firstName = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "autofocus":"autofocus"}) ,
                error_messages={'required': 'This field is required'})
        lastName = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "required":"required", "autofocus":"autofocus"}),
                error_messages={'required': 'This field is required'})
        username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control", "required":"required", "autofocus":"autofocus"}),
                error_messages={'required': 'This field is required'})
        email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control", "autofocus":"autofocus"}), 
                error_messages={'required': 'This field is required', 'invalid' : 'Your email is invalid'})
        department = forms.ChoiceField(label="Department", choices=departmentList, widget=forms.Select(attrs={"class":"form-select form-select", "aria-label":".form-select-lg example"}))
        userLevel = forms.ChoiceField(label="User Type", choices=userLevelList, widget=forms.Select(attrs={"class":"form-select form-select", "aria-label":".form-select-lg example"}))
        class Meta:
                model = User
                fields = ['firstName', 'lastName', 'username', 'email', 'department', 'userLevel']

class passwordChangeForm(forms.ModelForm):
    # Define the form fields
    current_password = forms.CharField(label='Current password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_password = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    new_password_confirm = forms.CharField(label='Confirm new password', widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ['current_password', 'new_password', 'new_password_confirm']

    def clean(self):
        # Override the default clean() method to validate the new password
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        new_password_confirm = cleaned_data.get('new_password_confirm')
        if new_password and new_password_confirm and new_password != new_password_confirm:
            # The new password and confirmation do not match, so we can add an error to the form
            self.add_error('new_password_confirm', 'The passwords do not match')

class changeImageForm(ModelForm):
        upload = forms.ImageField(label = "Upload Display Picture", widget=forms.FileInput(attrs={"class":"form-control"},))

        class Meta:
                model = User
                fields = ['upload']

class addSubjectForm(ModelForm):
        code = forms.CharField(label = "Subject Code" , widget=forms.TextInput(attrs={"class":"form-control"}))
        title = forms.CharField(label = "Subject Title" , widget=forms.TextInput(attrs={"class":"form-control"}))
        units = forms.CharField(label = "Units" , widget=forms.NumberInput(attrs={"class":"form-control"}))
        course = forms.CharField(label = "Course" , widget=forms.TextInput(attrs={"class":"form-control"}))

        class Meta:
                model = Subject
                fields = ['code', 'title', 'units', 'course']
class addExtensionForm(ModelForm):
        code = forms.CharField(label = "Extension Code", widget=forms.TextInput(attrs={"class":"form-control"}))
        title = forms.CharField(label = "Extension Service Title", widget=forms.TextInput(attrs={"class":"form-control"}))
        service = forms.CharField(label = "Service by", widget=forms.TextInput(attrs={"class":"form-control"}))
        department = forms.ChoiceField(label = "Department", choices=departmentList, widget=forms.Select(attrs={"class":"form-control"}))

        class Meta:
                model = Extension
                fields = ['code', 'title', 'service', 'department']

class addResearchForm(ModelForm):
        statuses = (
        ('Ongoing','Ongoing'),
        ('Presented','Presented'),
        ('Published','Published'),)
        code = forms.CharField(label = "Research Code", widget=forms.TextInput(attrs={"class":"form-control"}))
        title = forms.CharField(label = "Research Title", widget=forms.TextInput(attrs={"class":"form-control"}))
        status = forms.ChoiceField(label = "Research status", choices=statuses, widget=forms.Select(attrs={"class":"form-control"}), initial="Status")
        file = forms.FileField(label = "Research File", widget=forms.ClearableFileInput(attrs={"class":"form-control"}))
        class Meta:
                model = Research
                fields = ['code', 'title', 'status', 'file']

class addAnnouncementForm(ModelForm):
        title = forms.CharField(label = "Announcement Title", widget=forms.TextInput(attrs={"class":"form-control"}))
        content = forms.CharField(label = "Announcement", widget=forms.Textarea(attrs={"class":"form-control"}))

        class Meta:
                model = Announcement
                fields = ['title','content']

class addAuthResearchForm(ModelForm):
        statuses = (
        ('Ongoing','Ongoing'),
        ('Presented','Presented'),
        ('Published','Published'),)
        code = forms.CharField(label = "Research Code", widget=forms.TextInput(attrs={"class":"form-control"}))
        title = forms.CharField(label = "Research Title", widget=forms.TextInput(attrs={"class":"form-control"}))
        status = forms.ChoiceField(label = "Research status", choices=statuses, widget=forms.Select(attrs={"class":"form-control"}),initial="Status")
        file = forms.FileField(label = "Research File", widget=forms.ClearableFileInput(attrs={"class":"form-control"}))

        # def clean_pdf_file(self):
        #         file = self.cleaned_data['file']
        #         if not file.name.endswith('.pdf'):
        #                 raise forms.ValidationError("The file must be a PDF file.")
        #         return file
        class Meta:
                model = Research
                fields = ['code', 'title', 'status', 'file']