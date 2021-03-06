# Generated by Django 3.1 on 2020-10-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('img', models.ImageField(upload_to='media/')),
                ('content', models.TextField(max_length=100)),
            ],
        ),
    ]
