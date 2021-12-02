from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tool
from django.contrib.auth.views import LoginView



# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def tools_index(request):
  tools = Tool.objects.all()
  # similar to tool.find({}) in MEN stack
  return render(request, 'tools/index.html', {'tools': tools})

def tools_detail(request, tool_id):
  tool = Tool.objects.get(id=tool_id)
  return render(request, 'tools/detail.html', { 'tool': tool })
  

class toolCreate(CreateView):
  model = Tool
  fields = ['name', 'manufacturer', 'modelNumber', 'description']

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class toolUpdate(UpdateView):
  model = Tool
  # Let's disallow the renaming of a tool by excluding the name field!
  fields = ['manufacturer', 'modelNumber', 'description']

class toolDelete(DeleteView):
  model = Tool
  success_url = '/tools/'

