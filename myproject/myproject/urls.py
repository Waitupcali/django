"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views 
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views #views가 blog 껀지 accounts 껀지 모르니까 이름을 바꿔 준다.
from django.contrib.auth.views import LoginView, LogoutView #장고가 제공하는 log-in / log-out 기능을 사용.



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name = "index"),
    path('posting/', myapp.views.posting, name = "posting"),
    path('detail/<int:post_id>', myapp.views.detail, name = "detail"), #detail/<int:post_is> 가오면 blog.views.detail함수를 사용하고 그 이름을 detail이라고 해보자
    path('update/<int:post_id>', myapp.views.update, name = "update"),
    path('delete/<int:post_id>', myapp.views.delete, name = "delete"),
    path('accounts/signup/', accounts_views.signup, name="signup"),
    path('accounts/login', LoginView.as_view(), name="login"),
    path('accounts/logout', LogoutView.as_view(), name="logout"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

#여기서 아이디의 이름을 정해주는 거임
#이거를 views 에서 parameter name으로 받음
