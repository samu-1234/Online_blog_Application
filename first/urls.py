from turtle import home
from django.contrib import admin
from django.urls import path
# from first import views
from .import views
from first.form import BlogForm
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('',views.index, name='home'),
   path('signup/',views.signup, name='signup'),
   path('signup/register', views.register, name='register'),
   #changed by samruddhi
   path('saveRegister/',views.saveRegister,name='saveRegister'),
   path('login/savelogin',views.savelogin,name='savelogin'),
   #upto these
   #22/3/22
   path('check/',views.check),
   #upto this
   path('login/',views.login, name='login'),
   path('login/logout',views.logout,name='logout'),
   #26/6/22
   # path('login/savelogin/start',views.start,name='start'),
   path('login/loadform',views.load_form,name='loadform'),
   path('showdata',views.showdata,name='showdata'),
   path('login/showdatainlogin',views.showdatainlogin,name='showdatainlogin'),
   path('login/technologyinlogin',views.technologyinlogin,name='technologyinlogin'),
   path('login/socialmediainlogin',views.socialmediainlogin,name='socialmediainlogin'),
   path('login/onlinemaretinginlogin',views.onlinemaretinginlogin,name='onlinemaretinginlogin'),
   path('login/writtinginlogin',views.writtinginlogin,name='writtinginlogin'),

   
   path('saveform',views.saveform,name='saveform'),
   path('blog_detail/<int:id>',views.blog_detail,name='blog_detail'),
   path('blog_detailstype/<int:id>',views.blog_detailstype,name='blog_detailstype'),
   path('blogs_comments',views.blogs_comments,name='blogs_comments'),
   #upto this
   path('online marketing/',views.onlinemareting,name='onlinemarketing'),
   path('social media/',views.socialmedia,name='social media'),
   path('technology/',views.technology, name= 'technology'),
   path('writting/',views.writting,name='writting'),


   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)