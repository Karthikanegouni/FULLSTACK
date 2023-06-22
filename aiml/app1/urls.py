from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('hello',views.ok)
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('login_fun',views.login_fun),
    path('contact/feedback',views.feedback),
    path('registration/Insert_rec',views.Insert_rec),
    path('home/',views.home,name="home"),
    path("career/",views.career,name="career"),
    path("course/",views.courses,name="courses"),
    path("gadgets/",views.Gadgets,name="gadgets"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    # path("login/",views.login,name="login"),
    path("registration/",views.registration,name="registration"),


]
