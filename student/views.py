from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import student

# Create your views here.

class NewCourseView(CreateView):
    model = student
    fields = '__all__'


class ListCourseView(ListView):
    model = student
    context_object_name = 'student_list'

class UpdateCourseView(UpdateView):
    model = student
    fields = '__all__'


class DeleteCourseView(DeleteView):
    model = student
    success_url = "/ham/view"

# model_confirm_delete.html
