from django.urls import path

from . import views

urlpatterns = [
    # ex: /Hotel/
    path('', views.index, name='index'),
    path('<int:user_id>/<int:id>/<slug:slug>/', views.reservationhotel, name='Reservation_Form'),
    #path('reservationcancel/<int:user_id>/<int:id>/<slug:slug>', views.cancellationhotel, name='Cancellation_Form'),

    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
]
