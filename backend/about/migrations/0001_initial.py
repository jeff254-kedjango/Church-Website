# Generated by Django 4.2.1 on 2023-06-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='Enter title', max_length=225, verbose_name='title')),
                ('more', models.TextField(help_text='Explain yourself')),
            ],
            options={
                'verbose_name': 'Pillar Statement',
                'verbose_name_plural': 'Pillar Statements',
            },
        ),
        migrations.CreateModel(
            name='Dailydevotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='Your Name', max_length=225, verbose_name='name')),
                ('verse', models.TextField(help_text='Enter Verse')),
                ('devotion', models.TextField(help_text='Enter devotion')),
                ('video', models.FileField(blank=True, null=True, upload_to='images')),
            ],
            options={
                'verbose_name': 'Devotion',
                'verbose_name_plural': 'Devotions',
            },
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text='tile', max_length=225, verbose_name='title')),
                ('notice', models.TextField(help_text='Enter notice')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
            options={
                'verbose_name': 'Notice',
                'verbose_name_plural': 'Notices',
            },
        ),
    ]
