from django.shortcuts import render,redirect
# from django.views.generic import 
# from django.urls import reverse
from .models import Student
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
class StudentCreateView(CreateView):
    model=Student
    fields=['name','roll_no']
    success_url="/"

class StudentListView(ListView):
    model=Student
    # fields=['name','roll_no']

class StudentDetailView(DetailView):
    model = Student

class StudentUpdateView(UpdateView):
    model=Student
    fields=['name','roll_no']
    success_url=""

class StudentDeleteView(DeleteView):
    model=Student
    success_url='/'