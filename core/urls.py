from django.urls import path,include

from . import views
urlpatterns=[
    path("",views.homeview , name="home"),
    path("register",views.registerview , name="register"),
    path("login/",views.apploginview , name="login"),

    path("dashboard",views.dashboardview , name="dashboard"),
]