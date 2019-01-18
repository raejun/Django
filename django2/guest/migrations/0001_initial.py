# Generated by Django 2.1.2 on 2018-12-18 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('content', models.CharField(max_length=1000, verbose_name='내용')),
                ('write_date', models.TimeField(auto_now_add=True, verbose_name='날짜')),
            ],
        ),
    ]
