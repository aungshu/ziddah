from xml.dom.minidom import Attr
from django.core import validators
from django import forms
import datetime
from django.forms import ModelForm

#from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget
from .models import Daily_Expences, Daily_Incomes
#from bootstrap_datepicker_plus import DatePickerInput

class DateInput(forms.DateInput):
    input_type =  'date'

class DailyIncome(forms.ModelForm):
    class Meta:
        model = Daily_Incomes
        fields = ['Transaction_Date','Office_ID','Income_ID','Receipt_ID','Received_Amount',
                  'Remarks','Transaction_Made_BY','Updated_User_ID','Update_Date']
        labels ={
            'Transaction_Date': 'Date of Transaction',
            'Office_ID': 'Office Name',
            'Income_ID': 'Income Type',
            'Receipt_ID': 'Receipt No.',
            'Received_Amount':'Amount',
            'Remarks': 'Remarks (If Any)',
            }
        widgets = {
              'Transaction_Date': DateInput(attrs={'class': 'form-control','value':datetime.date.today()}),
              'Office_ID': forms.Select(attrs={'class': 'form-control'}),
              'Income_ID': forms.Select(attrs={'class': 'form-control'}),
              'Receipt_ID': forms.TextInput(attrs={'class': 'form-control'}),
              'Received_Amount': forms.TextInput(attrs={'class': 'form-control'}),
              'Remarks': forms.TextInput(attrs={'class': 'form-control'}),
              'Transaction_Made_BY':forms.HiddenInput(attrs={'class':'form-control','value':'Kazi Deen Mohammad'}),
              'Updated_User_ID':forms.HiddenInput(attrs={'class':'form-control', 'value':'1'}),
              'Update_Date':forms.HiddenInput(attrs={'class':'form-control','value':datetime.date.today()}),
              
       }

# Input forms for daily expenditure
class DailyExpences(forms.ModelForm):
    class Meta:
        model = Daily_Expences
        fields = ['Expence_Date','Office_ID','Expence_ID','Receiver_ID','Expend_Amount','Transaction_Made_BY',
                  'Updated_User_ID','Update_Date','Remarks']
        labels = {
            'Expence_Date':'Date of Expences',
            'Office_ID':'Office',
            'Expence_ID':'Expence Type',
            'Receiver_ID':'Paid to',
            'Expend_Amount':'Amount',
            'Remarks':'Remarks',
        }
        widgets = {
              'Expence_Date': DateInput(attrs={'class': 'form-control','value':datetime.date.today()}),
              'Office_ID': forms.Select(attrs={'class': 'form-control'}),
              'Expence_ID': forms.Select(attrs={'class': 'form-control'}),
              'Receiver_ID': forms.Select(attrs={'class':'form-control'}),
              'Expend_Amount': forms.TextInput(attrs={'class': 'form-control'}),
              #'Remarks': forms.TextInput(attrs={'class': 'form-control'}),
              'Transaction_Made_BY':forms.HiddenInput(attrs={'class':'form-control','value':'Kazi Deen Mohammad'}),
              'Updated_User_ID':forms.HiddenInput(attrs={'class':'form-control', 'value':'1'}),
              'Update_Date':forms.HiddenInput(attrs={'class':'form-control','value':datetime.date.today()}),
              'Remarks': forms.TextInput(attrs={'class': 'form-control'}),
       }
# End of input daily expenditure