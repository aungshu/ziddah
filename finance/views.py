
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import DailyExpences, DailyIncome
from .models import Daily_Expences, Daily_Incomes
from django.contrib import messages




# Create your views here.
def add_show(request):
    dincome=Daily_Incomes.objects.all() # dincome = Daily Income 
    if request.method == 'POST':
        fm = DailyIncome(request.POST)
        if fm.is_valid():
            fm.save()
            #return HttpResponse("Value Added")
            return render(request, 'finance/add_show.html',{'form':fm, 'di':dincome})
    else:
        fm = DailyIncome()
    #dincome=Daily_Incomes.objects.all() # dincome = Daily Income  
    return render(request, 'finance/add_show.html', {'form':fm, 'di':dincome})
 
# This function is to delete data by specified ID
def delete_data(request,id):
     if request.method == 'POST':
         pi = Daily_Incomes.objects.get(pk=id)
         #pi = DailyIncome.object.get(pk=id)
         pi.delete()
         messages.success(request, "Data Deleted Successfully")
         return HttpResponseRedirect('/')
         
# End of the function delete data

# This function is for edit or update
def update_data(request,id):
    if request.method == 'POST':
        pi = Daily_Incomes.objects.get(pk=id)
        fm = DailyIncome(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Data Updaed Successfully")
    else:
        pi = Daily_Incomes.objects.get(pk=id)
        fm = DailyIncome(instance=pi)
    return render(request,'finance/edit.html', {'form':fm})


# End of the function for edit or update

# Start of Function for Enter Daily Expences
def add_show_exp(request):
    dexp=Daily_Expences.objects.all() # dexp = Daily Expences 
    if request.method == 'POST':
        fmx = DailyExpences(request.POST)
        if fmx.is_valid():
            fmx.save()
            #return HttpResponse("Value Added")
            messages.success(request, 'Data Added Successfully')
            return render(request, 'finance/add_show_exp.html',{'form':fmx, 'de':dexp})
    else:
        fmx = DailyExpences()
    #dincome=Daily_Incomes.objects.all() # dincome = Daily Income  
    return render(request, 'finance/add_show_exp.html', {'form':fmx, 'de':dexp})
# End of Function for Daily Expences

# This function is to delete data by specified ID from Expences
def delete_data_exp(request,id):
     if request.method == 'POST':
         pi = Daily_Expences.objects.get(pk=id)
         #pi = DailyIncome.object.get(pk=id)
         pi.delete()
         return HttpResponseRedirect('/add_show_exp')
# End of the function delete data

# This function is for edit or update Expences
def update_data_exp(request,id):
    if request.method == 'POST':
        pi = Daily_Expences.objects.get(pk=id)
        fmx = DailyExpences(request.POST, instance=pi)
        if fmx.is_valid():
            fmx.save()
            messages.success(request, "Data Entered Successfully")
    else:
        pi = Daily_Expences.objects.get(pk=id)
        fmx = DailyExpences(instance=pi)
    return render(request,'finance/editexp.html', {'form':fmx})


# End of the function for edit or update Expences


def aungshu(request):
    return HttpResponse("This is Aungshu URL")
