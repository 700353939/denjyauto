# Generated by Django 5.1.3 on 2024-12-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Brand'),
        ),
    ]