# Generated by Django 2.0.4 on 2018-05-16 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_customers', '0003_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dop', models.DateField()),
                ('cexpiry', models.DateField()),
                ('status', models.CharField(default='pending', max_length=20)),
                ('cid', models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Registration')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('efname', models.CharField(db_column='EFName', max_length=20)),
                ('elname', models.CharField(db_column='ELName', max_length=20)),
                ('eemailid', models.CharField(db_column='EEmailid', max_length=50)),
                ('pass_field', models.CharField(db_column='pass', max_length=50)),
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
            name='Login',
            fields=[
                ('eid', models.ForeignKey(db_column='eid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='general_customers.Employee')),
                ('efname', models.CharField(db_column='EFName', max_length=20)),
                ('pass_field', models.CharField(db_column='pass', max_length=20)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='rid',
            field=models.ForeignKey(db_column='rid', on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Resource'),
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
