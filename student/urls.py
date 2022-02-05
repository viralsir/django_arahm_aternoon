from django.urls import path
from .views import NewCourseView,ListCourseView,UpdateCourseView,DeleteCourseView

urlpatterns = [
  path('add/',NewCourseView.as_view(),name='newstudent'),
  path('view/',ListCourseView.as_view(),name='viewstudent'),
  path('edit/<int:pk>',UpdateCourseView.as_view(),name='editstudent'),
  path('delete/<int:pk>',DeleteCourseView.as_view(),name='deletestudent'),

]
