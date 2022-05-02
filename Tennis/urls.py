from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.aboutus,name='about'),
    path('services/',views.services,name='services'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('education/',views.education,name='education'),
    path('sports/',views.sports,name='sports'),
    path('tennis/',views.tennis,name='tennis'),
    path('packages/',views.packages,name='packages'),
    path('private/',views.private,name='private'),
    path('T&C/',views.T_C,name='T_C'),
]
