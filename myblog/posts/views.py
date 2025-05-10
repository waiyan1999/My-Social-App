from django.shortcuts import render
from posts.models import customer

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