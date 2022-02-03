from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import courses
# Create your views here.
class NewCourseView(CreateView):
        model = courses
        fields = '__all__'

#model_form.html
#courses_form.html

class ListCourseView(ListView):
        model = courses
        context_object_name = 'course_list'

#model_list.html
#courses_list.html
#ObjectList=courses.objects.all()