from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

def homepage(request):
    return render(request, 'home.html') 

 

def about(request):
    return render(request,'about.html')

def article_list(request):
    
    if 'q' in request.GET:
        q = request.GET['q'] 
        multiple_query = Q(Q(title__icontains=q))
        # articles=Article.objects.filter(title__icontains=q)
        articles=Article.objects.filter(multiple_query)
        categories = Category.objects.all()
    else:
        categories = Category.objects.all()
        articles = Article.objects.all().order_by('date')

    context = {
            'articles': articles,
            'categories':categories
        }
    return render(request, 'article_list.html',context)
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
             instance.person = request.user.profile
             instance.save()
             return redirect('list')
     else:
         form=forms.CreateArticle()
         return render(request,'article_create.html',{'form':form})
    #   return render(request, 'article_create.html')



def update_article(request, pk):
    article = Article.objects.get(id=pk)
    form = forms.CreateArticle(instance=article)
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('/')
              
          


    return render(request, 'article_create.html', {'form':form})

    
def delete_article(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('/')
    return render(request,'article_delete.html',{'article':article})


def profile(request):
    profile = request.user.profile
    
    form = forms.ProfileForm(instance=profile)
    

    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form':form
    }       

    
    
    return render(request,'profile.html',context)


def categories(request,pk):

    category = Category.objects.get(id=pk)
    articles = category.article_set.all()
    context = {
        'category':category,
        'articles':articles
    }


    return render(request, 'category.html',context)
