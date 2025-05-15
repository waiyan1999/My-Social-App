from django.shortcuts import render,redirect,HttpResponse
from posts.models import customer
from posts.forms import *

# Create your views here.

def customer_data(request):
    
    data = customer.objects.all()
    
    context = {'data':data}
    return render(request,'customer.html',context)

def post_detail(request,pk):
    data1 = customer.objects.filter(id=pk)
    data2 = customer.objects.get(id=pk)
    context = {'data1':data1,'data2':data2}
    return render(request,'detail.html',context)

def create_post(request):
    
    
    if request.method == "POST":
        # title = request.GET.get('title')
        # # photo = request.GET.file('photo')
        
        # body =  request.GET.get('post_body')
        
        title = request.POST.get('title')
        body =  request.POST.get('post_body')
        photo = request.FILES.get('photo')
        
        # print(title)
        # print(photo)
        # print(body)
        
        # query = customer.objects.create( title = title,body = body , photo = photo )
        
        query = customer.objects.create( title = title , photo = photo , body=body)
        
        print('Success')
        # return redirect(" {% url 'customer' %} ")
        
        return redirect('/customer/')
    
    # return render(request,'createform.html',{'fm':fm})
    return render(request,'createform.html')


# def createform(request):
#     fm = PostCreatForm()
#     return render(request,'createform.html',{'fm':fm})

def createform(request):
    
    fm = PostModelform()
    
    if request.method == "POST":
        
        fm=PostModelform(request.POST,request.FILES)
        
        if fm.is_valid():
            print(fm)
            fm.save()
            return redirect('/customer/')
        
        else:
            print("error having")
            return HttpResponse('Error')
            
            
    return render(request,'createform.html',{'fm':fm})




# ========================== Day 10 =========================

def create_blog(request):
    
    form = BlogModelForm()
    context = {'form':form}
    return render(request, 'createblog.html', context)


def saveblog(request):
    form = BlogModelForm()
    if request.method == 'POST':
        form = BlogModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('Blog successfully saved !')
            return redirect('createblog') 
        
        else:
            return HttpResponse('Error Occur !!!!!!!!!!!!!!!')
        
        
        
        
    
    
def blog_list(request):
    data = customer.objects.all()
    context = {'data':data}
    return render(request,'bloglist.html',context)
        
    
def blog_detail(request,id):
    detail_data = customer.objects.filter(id=id)
    context = {'detail_data':detail_data}
    return render(request,'blogdetail.html',context)    
        
        
def delete_blog(request,id):
    delete_data = customer.objects.filter(id=id)
    delete_data.delete()
    return redirect('bloglist')