# Generated by Django 3.2 on 2022-11-25 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.CharField(blank=True, max_length=99, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=99)),
                ('email', models.EmailField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=99)),
                ('email', models.EmailField(max_length=199)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=500)),
                ('issue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.issue')),
            ],
        ),
    ]
