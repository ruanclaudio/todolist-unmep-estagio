# Generated by Django 4.1.3 on 2024-01-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='data',
            field=models.DateField(null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]
