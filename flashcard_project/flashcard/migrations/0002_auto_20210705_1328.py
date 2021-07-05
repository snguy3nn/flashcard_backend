# Generated by Django 3.1.8 on 2021-07-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='answer',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='question',
            field=models.CharField(max_length=150),
        ),
    ]
