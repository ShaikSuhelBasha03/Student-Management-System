from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
# Create your views here.
from App.models import Student

def student_list(request):
    student_details = Student.objects.all()
    return render(request,"student_list.html",{"student_details":student_details})


def single_student(request,id):
    details = get_object_or_404(Student,id=id)
    return render (request,"view_std.html",{"details":details})

from App.forms import StudentForm

def add_student(request):
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Student Details Added Successfully")
            form = StudentForm()
            return redirect("main")
        
        else:
            messages.error(request,"Please Provide Valid Details")
    
    else:
        form = StudentForm()    
    return render(request,"add_std.html",{"form":form})     


def update_student(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Details Updated Successfully")
            form = StudentForm()  
            return redirect("main")
        else:
            messages.error(request,"Something Went Wrong!")
    
    else:
        form = StudentForm(instance=student) 
    
    return render(request,"update_std.html",{"form":form,"student":student})  



def delete_student(request,id):
    students = get_object_or_404(Student,id=id) 
    if request.method =="POST":
        students.delete()
        messages.success(request,"Student Deleted Sucessfully")
        return redirect("main")
    # else:
    #     messages.error(request,"Something Went Wrong")    
    
    return render(request,"delete_std.html",{"students":students})            


def main(request):
    return render(request,"index.html")