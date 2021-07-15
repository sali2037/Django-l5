from django.contrib import admin
from blog.models import topic,text,accessDate,User,UserProfileInfo
# Register your models here.
admin.site.register(topic)
admin.site.register(text)
admin.site.register(accessDate)
admin.site.register(UserProfileInfo)
