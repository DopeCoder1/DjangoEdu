from django.urls import path
from .views import *

urlpatterns = [
    # path('',home,name='index'),
    path('',BlogHome.as_view(),name = 'index'),
    path('about/',about,name='about'),
    path('new_add_page',AddPage.as_view(), name = 'add_new_page'),
    # path('new_add_page/',new_add_form,name='add_new_page'),
    path('contact/',contact,name='contact'),
    path('login/',login,name='login'),
    path('post/<slug:post_slug>/',ShowPost.as_view(), name='post'),
    path('cat/<slug:category_slug>/', BlogCategory.as_view(), name='category'),
]
