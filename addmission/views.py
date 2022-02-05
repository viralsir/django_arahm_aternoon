from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from .models import addmissions
# Create your views here.
class NewAddmissionView(CreateView):
    model = addmissions
    fields = '__all__'

#model_form.html
class ListAddmissionView(ListView):
    model = addmissions
    context_object_name = 'addmissions'

class UpdateAddmissionView(UpdateView):
    model = addmissions
    fields = '__all__'

class DeleteAddmissionView(DeleteView):
    model = addmissions
    success_url = '/addmission/view'
