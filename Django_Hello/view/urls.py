from django.contrib import admin
from django.urls import path,include
from view import views

urlpatterns = [
    path('emps/',views.index),
    path('delete/',views.emp_delete),
    path('deletes/',views.emp_deletes),
    path('depts/',views.depts),
    path('addemp/',views.addemp),
    path('queryemp/',views.query_emp),
    path('modifyemp/',views.modify_emp),
    path('pages/',views.pages)
]