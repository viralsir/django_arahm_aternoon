from django.urls import path
from .views import NewCourseView,ListCourseView
urlpatterns=[
        path("new/",NewCourseView.as_view(),name="new-course"),
        path("view/",ListCourseView.as_view(),name="view-course")
]