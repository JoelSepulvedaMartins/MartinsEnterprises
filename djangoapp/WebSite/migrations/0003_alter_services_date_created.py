# Generated by Django 4.2.7 on 2023-11-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebSite', '0002_services_delete_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
