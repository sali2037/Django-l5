from django.db import models
#### level 5 django###############
from django.contrib.auth.models import User

# Create your models here.
class topic(models.Model):
    top_name=models.CharField(max_length=100)
    def __str__(self):
        return self.top_name

class text(models.Model):
    topic=models.ForeignKey(topic,on_delete=models.CASCADE)
    #users=models.ForeignKey(users,on_delete=models.CASCADE)
    title=models.TextField(blank=False)
    content=models.TextField(blank=False)
    def __str__(self):
        return self.content

class accessDate(models.Model):
    text=models.ForeignKey(text,on_delete=models.CASCADE)
    created_at=models.DateTimeField()
    modified=models.DateTimeField()
    def __str__(self):
        return self.created_at
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #aditional classes
    portfolio_site = models.URLField(blank= True)
    portfolio_pic  = models.FileField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username
