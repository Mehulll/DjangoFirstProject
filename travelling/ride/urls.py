from django.urls import path,include

from . import views

urlpatterns=[
    path('',views.index,name='index.html'),
    path('about/',views.about),
    path('news/',views.news),
    path('contact/',views.contact),
    path('booking/',views.booking),
    path('signup/',views.signup),
    path('login/',views.login),
    path('signup1/',views.signup1),
    path('destinations/',views.destination),

]