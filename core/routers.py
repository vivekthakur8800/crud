# from django.urls import path
# from .views import StudentCreateView,StudentListView,StudentDetailView,StudentUpdateView,StudentDeleteView
# app_name="core"
# urlpatterns=[
#     path("",StudentListView.as_view(),name="students"),
#     path("detail/<int:pk>",StudentDetailView.as_view(),name="student_detail"),
#     path("update/<int:pk>",StudentUpdateView.as_view(),name="student_update"),
#     path("add_student",StudentCreateView.as_view(),name="student_create"),
#     path("delete/<int:pk>",StudentDeleteView.as_view(),name="delete")
# ]

##########################################################################
from rest_framework import routers
from django.urls import path
from .views import StudentView
router=routers.DefaultRouter(trailing_slash=False)

# router.register("students",StudentView,basename="students")
urlpatterns=router.urls
urlpatterns+=[
    path("students",StudentView.as_view(),name="students"),
    path("students/<int:pk>",StudentView.as_view(),name="students"),
]