# Generated by Django 5.0.2 on 2024-03-31 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesnippet', '0002_projectoutput'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='student_images/')),
                ('roll_number', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='supervisor_images/')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('student1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student1', to='codesnippet.student')),
                ('student2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student2', to='codesnippet.student')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codesnippet.supervisor')),
            ],
        ),
    ]
