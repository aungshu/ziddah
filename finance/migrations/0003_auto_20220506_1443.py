# Generated by Django 3.1.4 on 2022-05-06 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_active_statuses_expenditure_types_income_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offices',
            name='Active_Status_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.active_statuses'),
        ),
    ]
