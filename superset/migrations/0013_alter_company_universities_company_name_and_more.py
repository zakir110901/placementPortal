# Generated by Django 4.1.7 on 2023-04-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superset', '0012_rename_company_name_company_universities_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_universities',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company_universities',
            name='universities',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
