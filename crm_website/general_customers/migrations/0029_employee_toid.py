# Generated by Django 2.0.4 on 2018-06-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_customers', '0028_employee_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='toid',
            field=models.CharField(default='', max_length=50),
        ),
    ]
