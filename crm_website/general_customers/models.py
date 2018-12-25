from django.db import models
from django.contrib.auth.models import User


class Registration(models.Model):
    cid = models.CharField(primary_key=True, max_length=20)
    firstname = models.CharField(db_column='firstName', max_length=20)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=20)  # Field name made lowercase.
    phoneno = models.BigIntegerField(db_column='phoneNo')  # Field name made lowercase.
    age = models.IntegerField()
    gender = models.TextField()  # This field type is a guess.
    cemailid = models.CharField(db_column='cEmailid', max_length=128)  # Field name made lowercase.
    loc = models.CharField(max_length=20)

    class Meta:
        db_table = 'registration'


class Employee(models.Model):
    eid = models.ForeignKey(User, models.DO_NOTHING, db_column='eid', primary_key=True)
    sales = models.IntegerField()
    pay = models.CharField(max_length=2, default='n')
    toid = models.CharField(max_length=50, default='')
    etherstopay = models.FloatField(default=0.00)

    class Meta:
        db_table = 'employee'

    def get_sales(self):
        return self.sales

class Resource(models.Model):
    rid = models.CharField(primary_key=True, max_length=20)
    rname = models.CharField(max_length=20)

    class Meta:
        db_table = 'Resource'


class Membership(models.Model):
    mid = models.CharField(primary_key=True, max_length=20)
    rid = models.ForeignKey(Resource, models.DO_NOTHING, db_column='rid')
    mname = models.CharField(max_length=20)
    mexpiry = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = 'membership'


class Customer(models.Model):
    cid = models.ForeignKey('Registration', models.DO_NOTHING, db_column='cid', blank=True, null=True)
    rid = models.ForeignKey('Resource', models.DO_NOTHING, db_column='rid', blank=True, null=True)
    mid = models.ForeignKey('Membership', models.DO_NOTHING, db_column='mid', blank=True, null=True)
    dop = models.DateField(blank=True, null=True)
    eid = models.ForeignKey('Employee', models.DO_NOTHING, db_column='eid', blank=True, null=True)
    cexpiry = models.DateField(blank=True, null=True)
    status=models.CharField(max_length=20, default='pending')

    class Meta:

        db_table = 'customer'

class Visitors(models.Model):
    product = models.CharField(db_column='product', max_length=20)  # Field name made lowercase.
    visitors = models.CharField(db_column='visitors', max_length=20)  # Field name made lowercase.
    avg_time = models.CharField(db_column='avg_time', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'visitors'
