from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tool
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def tools_index(request):
  tools = Tool.objects.filter(user=request.user)
  # similar to tool.find({}) in MEN stack
  return render(request, 'tools/index.html', {'tools': tools})

@login_required
def tools_detail(request, tool_id):
  tool = Tool.objects.get(id=tool_id)
  return render(request, 'tools/detail.html', { 'tool': tool })
  

class toolCreate(LoginRequiredMixin, CreateView):
  model = Tool
  fields = ['name', 'manufacturer', 'modelNumber', 'description']
  success_url = '/tools/' 

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class toolUpdate(LoginRequiredMixin, UpdateView):
  model = Tool
  # Let's disallow the renaming of a tool by excluding the name field!
  fields = ['manufacturer', 'modelNumber', 'description']

class toolDelete(LoginRequiredMixin, DeleteView):
  model = Tool
  success_url = '/tools/'    

def signup(request):
  error_message = ''
  if request.method == 'POST':

    form = UserCreationForm(request.POST)
    if form.is_valid():
      
      user = form.save()
      
      login(request, user)
      return redirect('tools_index')
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)