# Generated by Django 3.0.3 on 2020-04-26 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_claim', models.CharField(max_length=200, unique=True)),
                ('subject', models.CharField(max_length=40)),
                ('predicate', models.CharField(max_length=40)),
                ('object', models.CharField(max_length=40)),
                ('verdict', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('last_modification_date', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(to='newsapp.Category')),
                ('claims', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsapp.Claim')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
