from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from Home.forms import SignUpForm
from Home.models import Setting
from Hotel.models import Hotel, Category, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Hotel.objects.all()[:4]
    category=Category.objects.all()
    featureshotel = Hotel.objects.all().order_by('-id')[:6]
    recommendedhotels = Hotel.objects.all().order_by('?')[:3]
    context = {'setting': setting,
               'category':category,
               'page':'Home',
               'sliderdata': sliderdata,
               'featureshotel': featureshotel,
               'recommendedhotels': recommendedhotels, }

    return render(request, 'index.html', context)


def hotel_detail(request, id, slug):
    category = Category.objects.all()
    hotel = Hotel.objects.get(pk=id)
    images=Images.objects.filter(hotel_id=id)
    comments=Comment.objects.filter(product_id=id,status='True')
    context = {'hotel':hotel,
               'category':category,
               'images':images,
               'comments':comments,
               }
    return render(request,'hotel_detail.html',context)

def category_detail(request, id, slug):
    category=Category.objects.all()
    categorydata=Category.objects.get(pk=id)
    hotels= Hotel.objects.filter(category_id=id)
    context = {'hotels':hotels,
               'category':category,
               'categorydata':categorydata,
               }
    #return HttpResponse(mesaj)
    return render(request,'category_detail.html',context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"Kullanıcı Adı veya Şifre Hatalı Girildi !")
    category=Category.objects.all()
    context = {'category':category,
               }
    return render(request,'login.html',context)

def signup_view(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category=Category.objects.all()
    context = {'category':category,
               'form':form,
               }
    return render(request,'signup.html',context)
