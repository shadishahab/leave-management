# Generated by Django 3.2 on 2023-04-18 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0002_person_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='balance',
            field=models.SmallIntegerField(default=208),
        ),
        migrations.AddField(
            model_name='person',
            name='is_employer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
    ]