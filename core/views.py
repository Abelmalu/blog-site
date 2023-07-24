from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def homepage(request):
    return render(request, 'home.html') 

 

def about(request):
    return render(request,'about.html')

def article_list(request):
    articles=Article.objects.all().order_by('date')
    return render(request, 'article_list.html',{'articles':articles})
def article_detail(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request,'article_detail.html', {'article':article})


@login_required(login_url='/signup/login')
def article_create(request):
     if request.method=='POST':
         form=forms.CreateArticle(request.POST,request.FILES)
         if form.is_valid():
             instance = form.save(commit=False)
             instance.author=request.user
             instance.save()
             return redirect('list')
     else:
         form=forms.CreateArticle()
         return render(request,'article_create.html',{'form':form})
    #   return render(request, 'article_create.html')
      
