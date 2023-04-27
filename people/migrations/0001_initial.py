# Generated by Django 3.2 on 2023-04-03 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female')], null=True)),
                ('phone_no', models.CharField(max_length=11)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='companies.company')),
                ('job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobholders', to='companies.role')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
    ]
