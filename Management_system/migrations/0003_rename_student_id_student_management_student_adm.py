# Generated by Django 4.1.6 on 2023-09-24 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Management_system", "0002_student_management_student_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student_management",
            old_name="Student_id",
            new_name="Student_adm",
        ),
    ]