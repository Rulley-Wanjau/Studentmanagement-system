from django.shortcuts import render
from .models import Student_Management
from .forms import Student_Management_Form

# Create your views here.
def index(request):
    Student = Student_Management.objects.all()
    return render(request,"Management_system/index.html",{'Student':Student})


def Student_record(request,id):
    record = Student_Management.objects.get(pk=id)



def add_Student(request):
    if request.method == 'POST':
        form = Student_Management_Form(request.POST )

        if form.is_valid():
            new_Student_Adm = form.cleaned_data['Student_Adm'] 
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_year =form.cleaned_data['year']
            new_image =form.cleaned_data['image']

            email_verifier = Student_Management.objects.filter(email = new_email)
            if len(email_verifier) > 0:
                return render(request,"Management_system/message.html",{'message':'Please use another email,that email is already used in the system!'})
            else:
             New_Student = Student_Management(Student_Adm = new_Student_Adm,first_name =  new_first_name,last_name = new_last_name,email = new_email,field_of_study = new_field_of_study,year = new_year,image = new_image)
             New_Student.save()

             return render(request,"Management_system/add_student.html",{
                'form':form,
                'success':True
             })
        

    
    else:
     form = Student_Management_Form()
     return render(request,"Management_system/add_student.html",
                   {
                       'form':form
                       }
                   )
            



def about(request):

    
    return render(request,"Management_system/about.html",{'title':'About us page'})