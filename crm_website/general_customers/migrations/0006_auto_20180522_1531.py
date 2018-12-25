# Generated by Django 2.0.4 on 2018-05-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_customers', '0005_visitors'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('emails', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('sales', models.IntegerField()),
                ('eid', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'auth_user',
            },
        ),
        migrations.AlterField(
            model_name='registration',
            name='cemailid',
            field=models.CharField(db_column='cEmailid', max_length=128),
        ),
    ]