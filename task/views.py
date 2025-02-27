from django.shortcuts import render

# Create your views here.
def render_tasks(request):
    return render(request, 'tasks.html')