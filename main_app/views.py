from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Dog


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  # instantiate FeedingForm to be rendered in detail.html
  # feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', {
    'dog': dog 
  })

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'

class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs'
