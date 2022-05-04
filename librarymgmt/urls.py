"""librarymgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from library.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',About,name="about"),
    path('contact/',Contact,name="contact"),
    path('',Index,name="home"),
    path('admin_login/',Login,name="login"),
    path('logout/',Logout_admin,name="logout"),
    path('view_book/',View_Book,name="view_book"),
    path('add_book/',Add_Book,name="add_book"),
    path('delete_book(?P<int:pid>)',Delete_Book,name="delete_book"),
    path('view_student/',View_Student,name="view_student"),
    path('add_student/',Add_Student,name="add_student"),
    path('delete_student(?P<int:pid>)',Delete_Student,name="delete_student"),
    path('view_issuebook/',View_Issuebook,name="view_issuebook"),
    path('add_issuebook/',Add_Issuebook,name="add_issuebook"),
    path('delete_issuebook(?P<int:pid>)',Delete_Issuebook,name="delete_issuebook"),
    
    

]
