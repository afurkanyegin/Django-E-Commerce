from django.urls import path

from . import views

urlpatterns = [
    # ex: /Hotel/
    path('', views.index, name='index'),
    path('ReservationHotel/', views.ReservationHotel, name='ReservationHotel'), ]
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
