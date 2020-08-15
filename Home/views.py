from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.utils.crypto import get_random_string

from Home.forms import SignUpForm
from Home.models import Setting, UserProfile
from Hotel.models import Hotel, Category, Images, Comment
from reservation.models import ReservationForm, Reservation, ReservationHotel


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Hotel.objects.all()[:9]
    sliderdatamain =Hotel.objects.filter(gunluk_fiyat=899)
    category=Category.objects.all()
    tumoteller = Hotel.objects.order_by('bulundugu_il')
    featureshotel = Hotel.objects.all().order_by('-id')[:9]
    recommendedhotels = Hotel.objects.all().order_by('?')[:3]
    context = {'setting': setting,
               'category':category,
               'page':'Home',
               'sliderdata': sliderdata,
               'sliderdatamain': sliderdatamain,
               'featureshotel': featureshotel,
               'recommendedhotels': recommendedhotels,
               'tumoteller':tumoteller}

    return render(request, 'index.html', context)


def hotel_detail(request, id, slug):
    category = Category.objects.all()
    hotel = Hotel.objects.get(pk=id)
    images=Images.objects.filter(hotel_id=id)
    recommendedhotels = Hotel.objects.all().order_by('?')[:3]
    comments=Comment.objects.filter(hotel_id=id,status='True')
    context = {'hotel':hotel,
               'category':category,
               'images':images,
               'comments':comments,
               'recommendedhotels': recommendedhotels,
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

            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            return HttpResponseRedirect('/')

    form = SignUpForm()
    category=Category.objects.all()
    context = {'category':category,
               'form':form,
               }
    return render(request,'signup.html',context)

'''
@login_required(login_url='/login')
def reservationhotel(request,id,slug):
    category=Category.objects.all()
    hotel=Hotel.objects.get(pk=id)
    current_user = request.user
    total=0
    sayac=0
    gunsayisi=2
    total += hotel.gunluk_fiyat * gunsayisi
    if request.method =='POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            data = Reservation()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.country = form.cleaned_data['country']
            data.hotel = form.cleaned_data['hotel']
            data.startdate = form.cleaned_data['startdate']
            data.finishdate = form.cleaned_data['finishdate']
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            reservationcode = get_random_string(5).upper()
            data.code= reservationcode
            data.save()
            while (sayac==0):
                detail = ReservationHotel()
                detail.reservation_id = data.id
                detail.hotel_id = hotel.id
                detail.user_id=current_user.id
                sayac+=1

            detail.quantity = gunsayisi
            detail.price =hotel.gunluk_fiyat
            detail.amount=hotel.oda_sayisi
            detail.save()

            hotel.oda_sayisi -= 1
            hotel.save()

            messages.success(request, "Your reservation has been completed. Thank you")
            return render(request,'Reservation_Completed.html',{'reservationcode':reservationcode,'category':category,'hotel':hotel})
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect("/reservation/ReservationHotel")

    form=ReservationForm()
    profile =UserProfile.objects.get(user_id=current_user.id)
    context = {'category':category,
               'total':total,
               'gunsayisi':gunsayisi,
               'form':form,
               'profile':profile,
               'hotel':hotel,
               }
    return render(request,'Reservation_Form.html',context)
'''
