# Generated by Django 3.1 on 2020-08-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_vacancie_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancie',
            name='tasks',
            field=models.TextField(blank=True, null=True, verbose_name='Tasks'),
        ),
        migrations.AddField(
            model_name='vacancie',
            name='terms',
            field=models.TextField(blank=True, null=True, verbose_name='Terms'),
        ),
    ]