# Generated by Django 2.0.4 on 2018-05-23 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_customers', '0012_auto_20180523_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='eid',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='mid',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='rid',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='eid',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
