# Generated by Django 3.2 on 2023-04-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_confirmationcode_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmationcode',
            name='value',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
