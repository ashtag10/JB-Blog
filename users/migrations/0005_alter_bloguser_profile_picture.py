# Generated by Django 5.0.6 on 2024-07-24 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_bloguser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/profiles/'),
        ),
    ]
