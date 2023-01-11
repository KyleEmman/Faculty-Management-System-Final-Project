from django.db import models 
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import FileExtensionValidator

# class Login (models.Model):
#     pass
# sample announcement model

class User(AbstractUser):
    # username = models.CharField(max_length=30, unique=True)
    # password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, null=True ,blank=True)
    firstName = models.CharField(max_length=200, null=True ,blank=True)
    lastName = models.CharField(max_length=200, null=True ,blank=True)
    userLevel = models.IntegerField(null=True ,blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)

    upload = models.ImageField(default='defaultProfilePicture.png',upload_to='profilePictures', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email

class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Log(models.Model):
    name = models.CharField(max_length=200)
    activity = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity

class Subject(models.Model):
    code = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    units = models.IntegerField()
    course = models.CharField(max_length=200)

    def __str__(self):
        return self.code

class Research(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    file = models.FileField(max_length=200, null=True, blank = True,upload_to='researches', validators=[FileExtensionValidator(['pdf'])])


    def __str__(self):
        return self.title

class Extension(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=200, null =True, blank=True)
    title = models.CharField(max_length=200, null =True, blank=True)
    service = models.CharField(max_length=200, null =True, blank=True)
    department = models.CharField(max_length=200, null =True, blank=True)

    def __str__(self):
        return self.title
