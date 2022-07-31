from ast import Delete
from configparser import MAX_INTERPOLATION_DEPTH
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

#Start Model for Districts
class Districts(models.Model):
    District_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.District_Name

#End Model for Districts

#Start Model for Active Status
class Active_Statuses(models.Model):
    Active_Status_Name = models.CharField(max_length=20)
    Remarks = models.CharField(max_length=100)

    def __str__(self):
        return self.Active_Status_Name
# End Model for Active Status


# Start Model for Offices
class Offices(models.Model):
    Office_Name = models.CharField(max_length=100)
    Office_Address = models.TextField()
    District_ID = models.ForeignKey(Districts, null=True, on_delete=models.SET_NULL)
    Phone = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Active_Status_ID = models.ForeignKey(Active_Statuses, null=True, on_delete=models.SET_NULL)
    Remarks = models.CharField(max_length=200)

    def __str__(self):
        return self.Office_Name
# Start Model for Offices


#Start Model for Income Types
class Income_Types(models.Model):
    Income_Type_Name = models.CharField(max_length=100)
    Active_Status_ID = models.ForeignKey(Active_Statuses, null=True, on_delete=models.SET_NULL)
    Updated_Date = models.DateField()
    Update_User_ID = models.IntegerField(null=True)
    Remarks = models.CharField(max_length=100)

    def __str__(self):
        return self.Income_Type_Name
#End Model for Income Types

#Start Model for Expenditure Types
class Expenditure_Types(models.Model):
    Expenditure_Type_Name = models.CharField(max_length=100)
    Active_Status_ID = models.ForeignKey(Active_Statuses, null=True, on_delete=models.SET_NULL)
    Updated_Date = models.DateField()
    Update_User_ID = models.IntegerField(null=True)
    Remarks = models.CharField(max_length=100)

    def __str__(self):
        return self.Expenditure_Type_Name
#  End Model for Expenditure Types

#Start Model Receivables
class Incomes(models.Model):
    Income_Name = models.CharField(max_length=100)
    Income_Type_ID = models.ForeignKey(Income_Types, null=True, on_delete=models.SET_NULL)
    Active_Status_ID = models.ForeignKey(Active_Statuses, null=True, on_delete=models.SET_NULL)
    Update_User_ID = models.IntegerField()
    Update_Date = models.DateField()
    Remarks = models.CharField(max_length=100)

    def __str__(self):
        return self.Income_Name
#End of Model Receivables

#Start Model Expences
class Expences(models.Model):
    Expence_Name = models.CharField(max_length=100)
    Expenditure_Type_ID = models.ForeignKey(Expenditure_Types, null=True, on_delete=models.SET_NULL)
    Active_Status_ID = models.ForeignKey(Active_Statuses, null=True, on_delete=models.SET_NULL)
    Update_User_ID = models.IntegerField()
    Update_Date = models.DateField()
    Remarks = models.CharField(max_length=100)

    def __str__(self):
        return self.Expence_Name
#End of Model Expences

#Start Model Daily_Incomes
class Daily_Incomes(models.Model):
    Transaction_Date = models.DateField()
    Receipt_ID = models.IntegerField()
    Income_ID = models.ForeignKey(Incomes,null=True, on_delete=models.SET_NULL)
    Office_ID = models.ForeignKey(Offices, null=True, on_delete=models.SET_NULL)
    Received_Amount = models.IntegerField()
    Transaction_Made_BY = models.CharField(max_length=100, null=True)
    Updated_User_ID = models.IntegerField(null=True)
    Update_Date = models.DateField(null=True)
    Remarks = models.CharField(max_length=100, null=True)

   # def __str__(self):
    #    return self.Receipt_ID

#End Model Daily_Incomes

#Start Model Daily Expences
class Daily_Expences(models.Model):
    Expence_Date = models.DateField()
    Office_ID = models.ForeignKey(Offices, null=True, on_delete=models.SET_NULL)
    Expence_ID = models.ForeignKey(Expences, null=True, on_delete=models.SET_NULL)
    Expend_Amount = models.IntegerField()
    Transaction_Made_BY = models.CharField(max_length=100, null=True)
    Updated_User_ID = models.IntegerField(null=True)
    Update_Date = models.DateField(null=True)
    Remarks = models.CharField(max_length=100,)

    #def __str__(self):
     #   return self.Expend_Amount

#End of Model Daily Expences