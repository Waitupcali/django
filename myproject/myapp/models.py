from django.db import models
from django.utils import timezone

# Create your models here.

# model이라는 것을 상속받아 model이라는 것을 알려주는 것임

class Blog(models.Model): 
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    created_at = models.DateField(default = timezone.now)
    # myimage = models.ImageField(default = "null")
    myimage = models.FileField(upload_to = 'post', default = "hello") 

    #upload되는 이미지들이 들어갈 경로를 설정해주는 것이여

def __str__(self):
    return self.title