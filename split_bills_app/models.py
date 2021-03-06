# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class BillType(models.Model):
    cod_bill_type = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=100, db_column='type')

    class Meta:
        db_table = 'bill_type'
        managed = True
    
    def __str__(self):
        return self.name

class House(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, db_column='user_id')
    cod_house = models.AutoField(primary_key=True)
    adress = models.CharField(max_length=255)
    nick_name = models.CharField(blank=True, null=True, max_length=100)

    class Meta:      
        db_table = 'house'
    
    def __str__(self):
        return self.nick_name    


class Bills(models.Model):
    cod_bills = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    amount = models.TextField(blank=True, null=True)  # This field type is a guess.
    dead_line = models.DateField(blank=True, null=True)
    attachment = models.BinaryField(blank=True, null=True)
    paid_day = models.DateField(blank=True, null=True)
    cod_house = models.ForeignKey(House, models.DO_NOTHING, db_column='cod_house')
    dt_from = models.DateField(blank=True, null=True)
    dt_to = models.DateField(blank=True, null=True)
    cod_bill_type = models.ForeignKey(BillType, models.DO_NOTHING, db_column='cod_bill_type')
    send = models.BooleanField(blank=True, null=True)
    mime_type_old = models.CharField(blank=True, null=True, max_length=10)
    mime_type_res = models.CharField(blank=True, null=True, max_length=10)
    mime_type_99 = models.CharField(db_column='MIME_TYPE_99', blank=True, null=True, max_length=10)  # Field name made lowercase.
    mime_type = models.CharField(blank=True, null=True, max_length=10)

    class Meta:
        db_table = 'bills'
        verbose_name_plural = 'Bills'
    
    def __str__(self):
        return self.name
 
 
class Residents(models.Model):
    cod_resident = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=255)
    couple = models.BooleanField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=100)
    mobile = models.CharField(blank=True, null=True, max_length=100)
    cod_house = models.ForeignKey(to=House, on_delete=models.PROTECT, db_column='cod_house', verbose_name='House')
    dt_in = models.DateField(blank=True, null=True)
    dt_out = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'residents'
        verbose_name_plural = 'Residents'
    
    def __str__(self):
        return self.name
    
class Split(models.Model):
    cod_split = models.AutoField(primary_key=True)
    amount = models.FloatField(blank=True, null=True)  # This field type is a guess.
    split_date = models.DateField(blank=True, null=True)
    payed_day = models.DateField(blank=True, null=True)
    cod_bills = models.ForeignKey(Bills, models.DO_NOTHING, db_column='cod_bills')
    cod_resident = models.ForeignKey(Residents, models.DO_NOTHING, db_column='cod_resident')

    class Meta:
        db_table = 'split'
    
    def __str__(self):
        return self.cod_split