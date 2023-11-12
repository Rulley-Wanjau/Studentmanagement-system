from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('<int:id>',views.Student_record,name="student_record"),
    path('add/',views.add_Student,name="add"),
    path('about/',views.about,name="about"),
]