# from django.shortcuts import render,redirect
# # from django.views.generic import 
# from django.urls import reverse
# from .models import Student
# from django.views.generic.edit import CreateView,UpdateView,DeleteView
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# # Create your views here.
# class StudentCreateView(CreateView):
#     model=Student
#     fields=['name','roll_no']
#     success_url="/"

# class StudentListView(ListView):
#     model=Student
#     # fields=['name','roll_no']

# class StudentDetailView(DetailView):
#     model = Student

# class StudentUpdateView(UpdateView):
#     model=Student
#     fields=['name','roll_no']
#     success_url="/"

#     def get_success_url(self):
#         return reverse("core:students")

# class StudentDeleteView(DeleteView):
#     model=Student
#     success_url='/'
##########################################################################

from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# class StudentView(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

class StudentView(APIView):
    def get(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        if pk:
            queryset=get_object_or_404(Student,id=pk)
            serializer=StudentSerializer(queryset)
        else:
            queryset=Student.objects.all()
            serializer=StudentSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)
    
    def put(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        queryset=get_object_or_404(Student,id=pk)
        serializer=StudentSerializer(queryset,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def patch(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        queryset=get_object_or_404(Student,id=pk)
        serializer=StudentSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request,*args,**kwargs):
        pk=kwargs.get('pk')
        queryset=get_object_or_404(Student,id=pk)
        queryset.delete()
        return Response({"data":"deleted successfully"})