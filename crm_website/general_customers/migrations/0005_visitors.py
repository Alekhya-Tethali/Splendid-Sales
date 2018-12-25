# Generated by Django 2.0.4 on 2018-05-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_customers', '0004_auto_20180516_1103'),
    ]

    operations = [
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
    ]