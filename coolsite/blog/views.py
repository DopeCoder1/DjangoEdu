from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404
from .models import Blog
# Create your views here.

menu = [
    {'title':'О сайте','url_name':'about'},
    {'title':'Добавить статью','url_name':'add_page'},
    {'title':'Обратная связь','url_name':'contact'},
    {'title':'Войтиc','url_name':'login'},
]

def home(request):
    posts = Blog.objects.all()
    context = {
    'posts':posts,
    'menu':menu,
    'title':'Главная страница',
    }
    return render(request,'blog/index.html',context)


def about(request):
    context = {
    'title':'about site',
    'menu':menu,
    }
    return render(request,'blog/about.html',context)

def addpage(request):
    return HttpResponse('<h1>add page</h1>')

def contact(request):
    return HttpResponse('<h1>contact</h1>')

def login(request):
    return HttpResponse('<h1>login</h1>')

def show_post(request,post_id):
    return HttpResponse(f'<h1>show posts = {post_id} </h1>')

def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>Не найдено Лол)))</h1>")
