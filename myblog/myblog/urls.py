"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import customer_data,post_detail,create_post,createform,create_blog,saveblog,blog_list,blog_detail,delete_blog

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', customer_data, name = 'customer'),
    path('deatail/<int:pk>/',post_detail, name='detail'),
    path('createform/',create_post, name = "create_post"),
    path('form/',createform , name = 'form'),
    path('createblog/', create_blog, name = "createblog"),
    path('saveblog/', saveblog , name = 'saveblog'),
    path('bloglist',blog_list, name= 'bloglist'),
    path('blogdetail/<int:id>/', blog_detail, name= 'blogdetail'),
    path('deleteblog/<int:id>/',delete_blog, name= 'deleteblog'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
