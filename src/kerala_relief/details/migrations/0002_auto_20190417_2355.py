# Generated by Django 2.0.7 on 2019-04-17 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('donors', models.CharField(max_length=256)),
                ('raised', models.CharField(max_length=256)),
                ('exp', models.CharField(max_length=256)),
                ('countries', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='details',
        ),
    ]