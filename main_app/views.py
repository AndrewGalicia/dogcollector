from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog, Swag
from .forms import FeedingForm
import os

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def dogs_index(request):
  dogs = Dog.objects.filter(user=request.user)
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })

@login_required
def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  # First, create a list of the toy ids that the cat DOES have
  id_list = dog.swags.all().values_list('id')
  # Query for the toys that the cat doesn't have
  # by using the exclude() method vs. the filter() method
  swags_dog_doesnt_have = Dog.objects.exclude(id__in=id_list)
  # instantiate FeedingForm to be rendered in detail.html
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', {
    'dog': dog, 'feeding_form': feeding_form, 'swags': swags_dog_doesnt_have 
  })

class DogCreate(LoginRequiredMixin, CreateView):
  model = Dog
  fields = '__all__'

  def form_valid(self, form):
    #self.request.user is the logged in user
    form.instance.user = self.request.user
    #let the CreateView's for_valid method do it's regular work (saving the object and redirect)
    return super().form_valid(form)

class DogUpdate(LoginRequiredMixin, UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(LoginRequiredMixin, DeleteView):
  model = Dog
  success_url = '/dogs'

@login_required
def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)

class SwagsList(LoginRequiredMixin, ListView):
  model = Swag

class SwagsDetail(LoginRequiredMixin, DetailView):
  model = Swag

class SwagsCreate(LoginRequiredMixin, CreateView):
  model = Swag
  fields = '__all__'

class SwagsUpdate(LoginRequiredMixin, UpdateView):
  model = Swag
  fields = ['name', 'color']

class SwagsDelete(LoginRequiredMixin, DeleteView):
  model = Swag
  success_url = '/swags'

@login_required
def assoc_swag(request, dog_id, swag_id):
  Dog.objects.get(id=dog_id).swags.add(swag_id)
  return redirect('detail', dog_id=dog_id)

@login_required
def unassoc_swag(request, dog_id, swag_id):
  Dog.objects.get(id=dog_id).swags.remove(swag_id)
  return redirect('detail', dog_id=dog_id)  

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def some_function(request):
    secret_key = os.environ['SECRET_KEY']