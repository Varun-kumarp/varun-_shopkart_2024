from django.shortcuts import render
from . models import * 
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"shop/index.html ")

def register(request):
    return render(request,"shop/register.html")

def collection(request):
    catagorys=catagory.objects.filter(status=0)
    return render(request,"shop/collection.html",{"catagorys":catagorys})


def collectionview(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"shop/product/index.html",{"products":products,"category_name":name})
    else:
        messages.warning(request,"No such catagory found")
        return redirect('collection')