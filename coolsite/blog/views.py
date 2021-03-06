 from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound,Http404
from .models import *
from .forms import *
from django.views.generic import ListView,DetailView,CreateView
from django.urls import  reverse_lazy
# Create your views here.

menu = [
    {'title':'О сайте','url_name':'about'},
    {'title':'Добавить статью','url_name':'add_new_page'},
    {'title':'Обратная связь','url_name':'contact'},
    {'title':'Войти','url_name':'login'},
]

class BlogHome(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)

# def home(request):
#     posts = Blog.objects.all()
#
#     context = {
#     'posts':posts,
#     'menu':menu,
#     'title':'Главная страница',
#     'cat_selected':0,
#     }
#     return render(request,'blog/index.html',context)

# def new_add_form(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST,request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('index')
#     else:
#         form = AddPostForm()
#     return render(request, 'blog/new_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})
#

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'blog/new_page.html'
    success_url = reverse_lazy('index')

    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        return context

def about(request):
    context = {
    'title':'about site',
    'menu':menu,
    }
    return render(request,'blog/about.html',context)

# def addpage(request):
#     if(request.method == 'POST'):
#         form = AddPostForm(request.POST)
#         if(form.is_valid()):
#             try:
#                 Blog.objects.create(**form.cleaned_data)
#                 return redirect('index')
#             except :
#                 form.add_error(None, 'Ошибка ввода')
#     else:
#         form = AddPostForm()
#     context = {
#     'form':form,
#     'menu':menu,
#     }
#
#     return render(request,'blog/addpage.html',context=context)

def contact(request):
    return HttpResponse('<h1>contact</h1>')

def login(request):
    return HttpResponse('<h1>login</h1>')

# def show_post(request,post_slug):
#     post = get_object_or_404(Blog,slug = post_slug)
#     context={
#     'post':post,
#     'menu':menu,
#     'title':post.title,
#     'cat_selected':post.category_id,
#     }
#
#     return render(request,'blog/post.html',context=context)

class ShowPost(DetailView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg
    context_object_name = 'post'
    def show_category(request,cat_id):
        posts = Blog.objects.filter(category_id = cat_id)
        context={
        'posts':posts,
        'menu':menu,
        'title':'view site',
        'cat_selected':cat_id,
        }
        return context
        
    return render(request,'blog/index.html',context)

class BlogCategory(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Blog.objects.filter(category__slug=self.kwargs['category_slug'],is_published=True)

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].category)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].category_id
        return context

def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>Не найдено Лол)))</h1>")
