# Generated by Django 4.1.7 on 2023-03-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superset', '0002_alter_student_branch_alter_student_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]