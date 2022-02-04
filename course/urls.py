from django.urls import path
from .views import NewCourseView,ListCourseView,UpdateCourseView,DeleteCourseView
urlpatterns=[
        path("new/",NewCourseView.as_view(),name="new-course"),
        path("view/",ListCourseView.as_view(),name="view-course"),
        path("update/<int:pk>",UpdateCourseView.as_view(),name="update-course"),
        path("delete/<int:pk>",DeleteCourseView.as_view(),name="delete-course")
]