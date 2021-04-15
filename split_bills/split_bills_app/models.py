# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BillType(models.Model):
    cod_bill_type = models.AutoField(primary_key=True)
    type = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'bill_type'
    
    def __str__(self):
        return self.type


class Bills(models.Model):
    cod_bills = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=255)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    dead_line = models.DateField(blank=True, null=True)
    attachment = models.BinaryField(blank=True, null=True)
    paid_day = models.DateField(blank=True, null=True)
    cod_house = models.ForeignKey('House', models.DO_NOTHING, db_column='cod_house')
    dt_from = models.DateField(blank=True, null=True)
    dt_to = models.DateField(blank=True, null=True)
    cod_bill_type = models.ForeignKey(BillType, models.DO_NOTHING, db_column='cod_bill_type')
    send = models.BooleanField(blank=True, null=True)
    mime_type = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'bills'
    
    def __str__(self):
        return  self.name


class House(models.Model):
    cod_house = models.AutoField(primary_key=True)
    adress = models.CharField(max_length=255)
    nick_name = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        managed = True
        db_table = 'house'
    
    def __str__(self):
        return self.nick_name


class Invoices(models.Model):
    cod_invoice = models.AutoField(primary_key=True)
    cod_resident = models.ForeignKey('Residents', models.DO_NOTHING, db_column='cod_resident')
    cod_split = models.ForeignKey('Split', models.DO_NOTHING, db_column='cod_split')
    creation_date = models.DateField()
    due_date = models.DateField()
    paid_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'invoices'
    
    def __str__(self):
        return self.cod_invoice


class Residents(models.Model):
    cod_resident = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=255)
    couple = models.BooleanField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=255)
    mobile = models.CharField(blank=True, null=True, max_length=255)
    cod_house = models.IntegerField()
    dt_in = models.DateField()
    dt_out = models.DateField()

    class Meta:
        managed = True
        db_table = 'residents'

    def __str__(self):
        return self.name



class Split(models.Model):
    cod_split = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    split_date = models.DateField(blank=True, null=True)
    payed_day = models.DateField(blank=True, null=True)
    cod_bills = models.ForeignKey(Bills, models.DO_NOTHING, db_column='cod_bills')
    cod_resident = models.ForeignKey(Residents, models.DO_NOTHING, db_column='cod_resident')

    class Meta:
        managed = True
        db_table = 'split'
    
    def __str__(self):
        return  'Split'