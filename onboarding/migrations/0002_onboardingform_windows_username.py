# Generated by Django 4.2.16 on 2024-09-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onboardingform',
            name='windows_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
