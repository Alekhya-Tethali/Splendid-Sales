# Generated by Django 2.0.4 on 2018-05-16 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general_customers', '0002_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('cid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='firstName', max_length=20)),
                ('lastname', models.CharField(db_column='lastName', max_length=20)),
                ('phoneno', models.BigIntegerField(db_column='phoneNo')),
                ('age', models.IntegerField()),
                ('gender', models.TextField()),
                ('cemailid', models.CharField(db_column='cEmailid', max_length=20)),
                ('loc', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
    ]
