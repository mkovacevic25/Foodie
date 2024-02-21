# Generated by Django 4.2.7 on 2024-02-20 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_nutritivneinformacije_recept_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recept',
            name='nutritivne_informacije',
        ),
        migrations.AddField(
            model_name='nutritivneinformacije',
            name='recept',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.recept'),
        ),
    ]
