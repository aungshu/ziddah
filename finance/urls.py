from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name='add_show'),
    path('add_show_exp',views.add_show_exp, name='dexp'),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),
    path('deleteexp/<int:id>/',views.delete_data_exp,name='deleteexp'),
    path('update_data_exp/<int:id>/',views.update_data_exp,name='updateexp'),
    path('aungshu', views.aungshu, name='aungshu'),
]