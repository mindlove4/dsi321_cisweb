# Generated by Django 4.0.4 on 2022-05-14 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cisweb', '0004_student_student_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='cisweb.teacher'),
        ),
    ]
