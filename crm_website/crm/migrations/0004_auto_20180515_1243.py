# Generated by Django 2.0.4 on 2018-05-15 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20180515_1223'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Register',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]