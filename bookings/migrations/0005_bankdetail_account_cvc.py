# Generated by Django 5.1 on 2024-09-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_property_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetail',
            name='account_cvc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
