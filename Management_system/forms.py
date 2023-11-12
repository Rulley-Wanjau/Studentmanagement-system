from django import forms
from .models import Student_Management

class Student_Management_Form(forms.ModelForm):
      


    class Meta:
        model = Student_Management
        fields = '__all__'
        labels = {
            'Student_Adm':"Registration No",
            'first_name':'First Name',
            'last_name':'Last Name',
            'email':'Email',
            'field_of_study':'Field Of Study',
            'year':'Year',
            'image':'image'
        }
        widget = {
          'Student_Adm':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'field_of_study':forms.TextInput(attrs={'class':'form-control'}),
            'year':forms.NumberInput(attrs={'class':'form-control'}),
            'image':forms.ImageField()
        }
        
       
        