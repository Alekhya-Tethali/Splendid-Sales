# Generated by Django 2.0.4 on 2018-05-23 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('general_customers', '0020_auto_20180523_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dop', models.DateField()),
                ('cexpiry', models.DateField()),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.ForeignKey(db_column='eid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sales', models.IntegerField()),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('mid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=20)),
                ('mexpiry', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'membership',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('cid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='firstName', max_length=20)),
                ('lastname', models.CharField(db_column='lastName', max_length=20)),
                ('phoneno', models.BigIntegerField(db_column='phoneNo')),
                ('age', models.IntegerField()),
                ('gender', models.TextField()),
                ('cemailid', models.CharField(db_column='cEmailid', max_length=128)),
                ('loc', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('rid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('rname', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Resource',
            },
        ),
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(db_column='product', max_length=20)),
                ('visitors', models.CharField(db_column='visitors', max_length=20)),
                ('avg_time', models.CharField(db_column='avg_time', max_length=50)),
            ],
            options={
                'db_table': 'visitors',
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='rid',
            field=models.ForeignKey(db_column='rid', on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Resource'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cid',
            field=models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Registration'),
        ),
        migrations.AddField(
            model_name='customer',
            name='eid',
            field=models.ForeignKey(blank=True, db_column='eid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Employee'),
        ),
        migrations.AddField(
            model_name='customer',
            name='mid',
            field=models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Membership'),
        ),
        migrations.AddField(
            model_name='customer',
            name='rid',
            field=models.ForeignKey(db_column='rid', on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Resource'),
        ),
    ]
