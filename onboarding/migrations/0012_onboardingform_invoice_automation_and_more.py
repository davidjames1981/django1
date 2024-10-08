# Generated by Django 4.2.16 on 2024-09-15 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboarding', '0011_alter_onboardingform_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='onboardingform',
            name='invoice_automation',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='onboardingform',
            name='syspro_aft',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='onboardingform',
            name='syspro_int',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='onboardingform',
            name='syspro_man',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='onboardingform',
            name='warranty_system',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
    ]
