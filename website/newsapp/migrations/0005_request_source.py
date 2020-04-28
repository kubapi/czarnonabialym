# Generated by Django 3.0.3 on 2020-04-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_auto_20200428_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='source',
            field=models.CharField(choices=[('EX', 'Browser extension'), ('CF', 'Contact form')], default='EX', max_length=200),
            preserve_default=False,
        ),
    ]
