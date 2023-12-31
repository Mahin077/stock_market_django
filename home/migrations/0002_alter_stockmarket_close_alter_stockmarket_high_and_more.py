# Generated by Django 4.2.4 on 2023-08-31 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmarket',
            name='close',
            field=models.DecimalField(decimal_places=1, max_digits=8),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='high',
            field=models.DecimalField(decimal_places=1, max_digits=8),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='low',
            field=models.DecimalField(decimal_places=1, max_digits=8),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='open',
            field=models.DecimalField(decimal_places=1, max_digits=8),
        ),
        migrations.AlterField(
            model_name='stockmarket',
            name='trade_code',
            field=models.CharField(max_length=18),
        ),
    ]
