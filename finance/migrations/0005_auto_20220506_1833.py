# Generated by Django 3.1.4 on 2022-05-06 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_auto_20220506_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenditure_types',
            name='Active_Status_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.active_statuses'),
        ),
        migrations.AlterField(
            model_name='income_types',
            name='Active_Status_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.active_statuses'),
        ),
    ]
