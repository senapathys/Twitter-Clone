# Generated by Django 3.1.4 on 2020-12-09 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201207_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=280)),
                ('tweets', models.ManyToManyField(to='main.Tweet')),
            ],
        ),
    ]