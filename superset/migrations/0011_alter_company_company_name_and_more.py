# Generated by Django 4.1.7 on 2023-04-10 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superset', '0010_company_universities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Company_Name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='company_universities',
            name='Company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superset.company'),
        ),
        migrations.AlterField(
            model_name='company_universities',
            name='universities',
            field=models.CharField(max_length=100),
        ),
    ]