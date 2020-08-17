from django.urls import path

from . import views

urlpatterns = [
    # ex: /Hotel/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservationdetail/<int:id>', views.reservationdetail, name='reservationdetail'),
    #path('reservationcancel/<int:user_id>/<int:id>/<slug:slug>', views.cancellationhotel, name='Cancellation_Form'),
    path('cancel/', views.cancellation, name='cancel'),
]
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
