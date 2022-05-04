from django.db import models

# Create your models here.


class Book(models.Model):
    bookname=models.CharField(max_length=50)
    authorname=models.CharField(max_length=100)
    isbn=models.IntegerField()
    edition=models.IntegerField()
    publication=models.CharField(max_length=100)



    def __str__(self):
        return self.bookname


class Student(models.Model):
    studentname=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    semester=models.IntegerField()
    gender=models.CharField(max_length=10)
    mobile=models.IntegerField(null=True)
    address=models.CharField(max_length=60)
    
    


    def __str__(self):
        return self.studentname


class Issuebook(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    issuedate=models.DateField()
    returndate=models.DateField()
    time1=models.TimeField()    


    #def __str__(self):
        #return self.book.bookname+"--"+self.student.studentname
         #return self.book


        
