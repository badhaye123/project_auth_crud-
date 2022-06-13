from django.shortcuts import render,redirect
from .forms import  OrderModelForm
from .models import Books
from django.contrib import messages

#from django.contrib.auth.decorators import login_required
# Create your views here.


def testView(request):
    template_name = 'OrdersApp/base.html'
    context = {}
    return render(request,template_name,context)


def homeView(request):
    template_name = 'OrdersApp/home.html'
    context = {}
    return render(request,template_name,context)


def addBookView(request):
    form = OrderModelForm()    
    if request.method =='POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showbooks')
    template_name ='OrdersApp/addbook.html'
    context = {'form':form}
    return render(request,template_name,context)


def showBookView(request):
    pro = Books.objects.all()
    print(pro)
    template_name = 'OrdersApp/showbooks.html'
    context = {'pro':pro}
    return render(request,template_name,context)


def updateBookView(request,pk):
    pro = Books.objects.get(id=pk)
    form = OrderModelForm(instance=pro)
    if request.method == 'POST':
        form = OrderModelForm(request.POST,instance=pro)    
        if form.is_valid():
            form.save()
            print('data updated')
            return redirect('showbooks')
    template_name = 'OrdersApp/addbook.html'
    context = {'form':form}
    return render(request,template_name,context)
    

def deleteBookView(request,pk):
    pro = Books.objects.get(id=pk)
    pro.delete()
    print('data deleted')
    return redirect('showbooks') 
