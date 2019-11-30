from django.contrib import admin
from .models import Blog

# Register your models here.
# blot모델을 관리하려면 form같은게 있어야되는데 지금은 없으니까
# admin에 다가 등록해버리는 것이었다.
admin.site.register(Blog)