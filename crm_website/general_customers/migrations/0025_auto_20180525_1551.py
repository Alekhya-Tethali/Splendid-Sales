# Generated by Django 2.0.4 on 2018-05-25 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_customers', '0024_auto_20180525_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cexpiry',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='dop',
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
            name='status',
        ),
        migrations.AlterModelTable(
            name='customer',
            table=None,
        ),
    ]
