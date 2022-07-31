# Generated by Django 3.1.4 on 2022-05-06 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20220506_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='offices',
            name='District',
        ),
        migrations.AddField(
            model_name='offices',
            name='District_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.districts'),
        ),
    ]
