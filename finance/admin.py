from django.contrib import admin
from .models import Offices,Active_Statuses,Income_Types,Expenditure_Types,Districts, Incomes, Expences, Daily_Incomes, Daily_Expences

# Register your models here.
admin.site.register(Offices)
admin.site.register(Active_Statuses)
admin.site.register(Income_Types)
admin.site.register(Expenditure_Types)
admin.site.register(Districts)
admin.site.register(Incomes)
admin.site.register(Expences)
admin.site.register(Daily_Incomes)
admin.site.register(Daily_Expences)
