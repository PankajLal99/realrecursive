# Generated by Django 3.0.2 on 2020-06-09 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0006_auto_20200609_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='trainer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]