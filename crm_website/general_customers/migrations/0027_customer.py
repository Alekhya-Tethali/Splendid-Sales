# Generated by Django 2.0.4 on 2018-05-25 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general_customers', '0026_auto_20180525_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dop', models.DateField(blank=True, null=True)),
                ('cexpiry', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='pending', max_length=20)),
                ('cid', models.ForeignKey(blank=True, db_column='cid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Registration')),
                ('eid', models.ForeignKey(blank=True, db_column='eid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Employee')),
                ('mid', models.ForeignKey(blank=True, db_column='mid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Membership')),
                ('rid', models.ForeignKey(blank=True, db_column='rid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general_customers.Resource')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]