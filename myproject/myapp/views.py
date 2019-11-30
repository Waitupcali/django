from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    all_blog = Blog.objects.all() #al_Blog는 택배 상자여
    context = {"all_blog": all_blog}
    return render(request, 'index.html', context)

@login_required
def posting(request):
    #모델폼 기능이 들어갈 예정
    # mypostform = PostForm() #mypostform은 택배상자여

    if request.method =='POST':
        mypostform = PostForm(request.POST, request.FILES) #사용자가 보내는 request가 POST일 때
        if mypostform.is_valid: #valid 검사를 해라
            mypostform.save() 
            return redirect('index') #index라고 불리우는 url 요청을 보내라
        else: 
            return redirect('posting') 

    else: 
        mypostform = PostForm() #비어있는 폼을 보내는 것.
        context = {'mypostform': mypostform}
    
    return render(request,'posting.html', context)

    #내용
    #내가 Blogform을만들어 놨는데 그거를 myblog에 담아 놓을게 위에서
    #context라는 것을 만들어서 추가한 것과 같이

    #redirect랑 render의 차이
    #render는 url요청이 아닌 개발자가 이미 설정해놓은 그림을 보여주는 것과 같다.
    #redirect는 url요청을 받고 그 page를 띄우는 것임
    myblog = PostForm()
    context ={"myblog": myblog}
    return render(request, 'posting.html', context)

@login_required
def detail(request,post_id):
    # post_one = Post.objects.get(id=post_id)
    post_one = get_object_or_404(Blog, id = post_id)
    context = {"post_one" : post_one}
    return render(request, 'detail.html', context)


@login_required
def update(request, post_id):
    post = get_object_or_404(Blog, id=post_id)

    if request.method =='POST':
        mypostform = PostForm(request.POST, request.FILES, instance=post) #사용자가 보내는 request가 POST일 때 사용자가 바꾸고 싶은애를 지정해준것
        if mypostform.is_valid: #valid 검사를 해라
            mypostform.save() 
        return redirect('index') #index라고 불리우는 url 요청을 보내라

    else:
        mypostform = PostForm(instance=post)
        context = {"mypostform":mypostform}
        return render(request, 'update.html', context)

@login_required
def delete(request, post_id):
    my_post_one = get_object_or_404(Blog, id = post_id)
    my_post_one.delete()
    return redirect('index')