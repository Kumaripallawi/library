#from os import error
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login

# Create your views here.
def About(request):
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    book=Book.objects.all()
    student=Student.objects.all()
    issuebook=Issuebook.objects.all()

    b=0;
    s=0;
    ib=0;
    for i in book:
        b+=1
    for i in student:
        s+=1
    for i in issuebook:
        ib+=1
    b1={'b':b,'s':s,'i':ib}
    return render(request,'index.html',b1)


def Login(request):
    error=""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        User=authenticate(username=u,password=p)
        try:
            if User.is_staff:
               login(request,User)
               error='no'
            else:
                error='yes'
        except:
            error='yes'
    d = {'error':error}
    
    
    return render(request,'login.html',d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def View_Book(request):
    if not request.user.is_staff:
        return redirect('login')
    buk = Book.objects.all()
    b = {'buk':buk}
    return render(request,'View_Book.html',b)

def Add_Book(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        b = request.POST['bookname']
        a= request.POST['authorname']
        i= request.POST['isbn']
        e= request.POST['edition']
        p= request.POST['publication']
        try:
            Book.objects.create(bookname=b,authorname=a,isbn=i,edition=e,publication=p)
            error="no"
        except:
            error='yes'
    d = {'error':error}
    
    
    return render(request,'add_book.html',d)


def Delete_Book(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    book = Book.objects.get(id=pid)
    book.delete()
    return redirect('view_book')




def View_Student(request):
    if not request.user.is_staff:
        return redirect('login')
    stu = Student.objects.all()
    d = {'stu':stu}
    return render(request,'View_Student.html',d)

def Add_Student(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        sn= request.POST['studentname']
        b= request.POST['branch']
        s= request.POST['semester']
        g= request.POST['gender']
        m= request.POST['mobile']
        a= request.POST['address']
        try:
            Student.objects.create(studentname=sn,branch=b,semester=s,gender=g,mobile=m,address=a)
            error="no"
        except:
            error='yes'
    d = {'error':error}
    return render(request,'add_student.html',d)


def Delete_Student(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    book = Student.objects.get(id=pid)
    Student.delete()
    return redirect('View_Student')



def View_Issuebook(request):
    if not request.user.is_staff:
        return redirect('login')
    issue = Issuebook.objects.all()
    d = {'issue':issue}
    return render(request,'View_issuebook.html',d)

def Add_Issuebook(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    book1= Book.objects.all()
    student1 =Student.objects.all()

    if request.method == 'POST':
        b= request.POST['book']
        s= request.POST['student']
        i= request.POST['issuedate']
        r= request.POST['returndate']
        t= request.POST['time']
        book = Book.objects.filter(bookname=b).first()
        student = Student.objects.filter(studentname=s).first()
        
        
        try:
            Issuebook.objects.create(book=book,student=student,issuedate=i,returndate=r,time1=t)
            error="no"
        except:
            error='yes'
    d = {'book':book1,'student':student1,'error':error}
    
    
    return render(request,'add_issuebook.html',d)


def Delete_Issuebook(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    issuebook = Issuebook.objects.get(id=pid)
    issuebook.delete()
    return redirect('View_issuebook')