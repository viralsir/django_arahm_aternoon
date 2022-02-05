from django.urls import path
from .views import *

urlpatterns=[
    path("new/",NewAddmissionView.as_view(),name="new-addmission"),
    path("view/", ListAddmissionView.as_view(), name="view-addmission"),
    path("update/<int:pk>",UpdateAddmissionView.as_view(),name="update-addmission"),
    path("delete/<int:pk>",DeleteAddmissionView.as_view(),name="delete-addmission")

]