# Generated by Django 3.0.7 on 2020-10-14 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pravda_brain', '0002_auto_20201014_2220'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
