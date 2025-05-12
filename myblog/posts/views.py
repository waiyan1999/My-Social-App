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