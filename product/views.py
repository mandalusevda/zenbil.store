from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product1
from django.utils import timezone
# Create your views here.
@login_required(login_url="/accounts/login")
def my_home(request):
    return render(request, 'product/home2.html')
def detail(request):
    products=product1.objects.all
    return render(request, 'product/my_page.html',{'products':products})
def ListView(request):
    return render(request,'product/Home1.html')

# def detail2(request):
#     products2=product2.objects
#     return render(request, 'product/my_page.html',{'products2':products2})

def create(request):
    return render(request, 'product/create.html')
# @login_required(login_url="/accounts/login")
def postx(request):
    # if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['title'] and request.POST['size'] and request.FILES['pic'] :
                product = product1()
                product.title = request.POST['title']
                product.size = request.POST['size']
                product.body = request.POST['body']
                product.pic =request.FILES['pic']
                product.price=request.POST['price']
                product.cdate = timezone.datetime.now()
                product.User = request.user
                product.save()
                return redirect('product_post')
                # return render(request, 'product/my_page.html')
            else:
                return render(request, 'product/create.html',{'error':'fields can not be empty'})
        else:
            return render(request, 'product/create.html')
# def posty(request):
#     if request.method == 'POST':
#         if request.POST['title'] and request.POST['size'] and request.FILES['pic']:
#             product = product2()
#             product.name = request.POST['title']
#             product.size = request.POST['size']
#             product.caption = request.POST['body']
#             product.pic=request.POST['pic']
#             product.price=request.POST['price']
#             product.cdate = timezone.datetime.now()
#             # marketer.User = request.user
#             product.save()
#             return redirect('product_post')
#         else:
#             return render(request, 'product/my_page.html',{'error':'fields can not be empty'})
#     else:
#         return render(request, 'product/my_page.html')
