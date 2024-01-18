from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from  core.models import Profile

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            profile=Profile.objects.create(user=user)
            return redirect('login')
        
            
            
            
    else:

        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in user
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('list')

    

    else:
        form=AuthenticationForm()
    return render(request, 'login.html',{'form':form} )

def logout_view(request):
    
        logout(request)
        return redirect('list')

