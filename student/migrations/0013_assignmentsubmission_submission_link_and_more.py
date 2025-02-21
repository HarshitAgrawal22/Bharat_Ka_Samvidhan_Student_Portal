# Generated by Django 4.2.7 on 2024-06-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_alter_aiquestion_answer_alter_aiquestion_question_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmission',
            name='submission_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assignment_type',
            field=models.CharField(choices=[('Coding', 'Coding'), ('Text', 'Text'), ('File', 'File'), ('Image', 'Image'), ('Link', 'Link')], max_length=10),
        ),
    ]
