from django.http import HttpResponse
from django.shortcuts import render


# Главная страница
def index(request):    
    template = 'confapp/index.html'
    return render(request, template)

# Страница конфигурации R050 - пока работаю над ней
def r050_conf(request):    
    template = 'confapp/r050.html'
    return render(request, template)

# Страница конфигурации R500 - в планах разработки
def r500_conf(request):    
    return HttpResponse('Страница конфигурации R500')
# Страница конфигурации R500S - в планах разработки
def r500s_conf(request):    
    return HttpResponse('Страница конфигурации R500S')
# Страница конфигурации AR - в планах разработки
def ar_conf(request):    
    return HttpResponse('Страница конфигурации AR')