# Generated by Django 5.1.3 on 2024-11-30 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inscription',
            unique_together={('user', 'course')},
        ),
    ]
