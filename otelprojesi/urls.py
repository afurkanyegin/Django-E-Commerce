"""otelprojesi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Home import views

urlpatterns = [
    path('', include('Home.urls')),
    path('hotel/', include('Hotel.urls')),
    path('user/', include('user.urls')),
    path('reservation/', include('reservation.urls')),
    path('home/', include('Home.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('category/<int:id>/<slug:slug>/', views.category_detail, name='category_detail'),
    path('Hotel/<int:id>/<slug:slug>/', views.hotel_detail, name='hotel_detail'),
    #path('reservation/<int:id>/<slug:slug>/', views.reservationhotel, name='Reservation_Form'),
    #path('reservation/Res_Complete', views.reservationhotel, name='Reservation_Complete'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
