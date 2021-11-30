from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tool



# Create your views here.
def home(request):
  return render(request, 'home.html')

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
  fields = ['name', 'manufacturer', 'description']

class toolUpdate(UpdateView):
  model = Tool
  # Let's disallow the renaming of a tool by excluding the name field!
  fields = ['name', 'manufacturer', 'description']

class toolDelete(DeleteView):
  model = Tool
  success_url = '/tools/'

