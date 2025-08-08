from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

KOP_CHOISES = (
    ("YEN", "Юрченко Е.Н."),
    ("NTT", "Нагаев Т.Т."),
)
    

# Create your models here.
class Calculation(models.Model):
    deal_num = models.CharField(max_length=6) # номер сделки Битрикс
    integrator_name = models.CharField(max_length=30) # название интегратора (контрагент)
    object_name = models.TextField() # Название объекта (проекта)
    kop_name = models.CharField(choices=KOP_CHOISES) # представитель от КОП
    created_at = models.DateTimeField(auto_now_add=True) # Дата создания запроса (автоматом)
