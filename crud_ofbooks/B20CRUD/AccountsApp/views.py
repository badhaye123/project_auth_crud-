from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def loginView(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        ps = request.POST.get('password')

        user = authenticate(username=un,password=ps)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credential')    
    
    template_name= 'AccountsApp/login.html'
    return render(request,template_name)


def registerView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='AccountsApp/register.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required
def LogoutView(request):
    logout(request)
    return redirect('login')       
