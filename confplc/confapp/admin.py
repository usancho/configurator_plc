from django.contrib import admin
# Из модуля models импортируем модель Post
from .models import Calculation

class CalculationAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('deal_num', 'integrator_name', 'object_name', 'kop_name', 'created_at',) 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('integrator_name', 'object_name', 'kop_name', 'created_at',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

admin.site.register(Calculation, CalculationAdmin) 

