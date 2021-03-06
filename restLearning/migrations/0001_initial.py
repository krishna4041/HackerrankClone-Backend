# Generated by Django 2.0.5 on 2019-02-07 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=120)),
                ('problem_description', models.TextField()),
                ('problem_level', models.CharField(max_length=120)),
                ('problem_sampleInput', models.CharField(max_length=120)),
                ('problem_sampleOutput', models.CharField(max_length=120)),
                ('problem_main_file', models.FileField(upload_to='')),
                ('problem_testcase_file', models.FileField(upload_to='')),
                ('problem_body_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_box', models.CharField(max_length=100)),
            ],
        ),
    ]
