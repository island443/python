# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblDept(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tbl_dept'


class TblEmp(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    d = models.ForeignKey(TblDept, models.DO_NOTHING, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'tbl_emp'
        ordering = ['emp_id']
