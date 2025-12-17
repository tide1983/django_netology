from django.shortcuts import render
from django.http import HttpResponse
import datetime
import os

def home_view(request):
    pages = {
        'Главная страница': '/',
        'Текущее время': '/current_time/',
        'Содержимое рабочей директории': '/workdir/'
    }
    return render(request, 'home.html', {'pages': pages})

def current_time_view(request):
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {current_time}")

def workdir_view(request):
    files = os.listdir('.')
    
    dirs = [f for f in files if os.path.isdir(f)]
    files_only = [f for f in files if not os.path.isdir(f)]
    
    content = "<h1>Содержимое рабочей директории:</h1>"
    
    if dirs:
        content += "<h2>Папки:</h2><ul>"
        for d in sorted(dirs):
            content += f"<li>📁 {d}</li>"
        content += "</ul>"
    
    if files_only:
        content += "<h2>Файлы:</h2><ul>"
        for f in sorted(files_only):
            content += f"<li>📄 {f}</li>"
        content += "</ul>"
    
    return HttpResponse(content)