from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def signup(request):

    if request.method=="POST":

        save_form = UserCreationForm(request.POST)

        if save_form.is_valid:
            save_form.save()
            return redirect('index')
            
        else:
            return redirect('signup')    

    else:
        my_signup_form = UserCreationForm()

    context = {'my_signup_form':my_signup_form}
    return render(request, 'registration/signup.html', context)