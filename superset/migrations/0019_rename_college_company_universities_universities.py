# Generated by Django 4.1.7 on 2023-06-07 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superset', '0018_rename_universities_company_universities_college_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_universities',
            old_name='college',
            new_name='universities',
        ),
    ]