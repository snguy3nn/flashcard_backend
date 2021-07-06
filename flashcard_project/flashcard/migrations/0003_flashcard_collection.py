# Generated by Django 3.1.8 on 2021-07-06 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0002_auto_20210705_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='collection',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flashcard.collection'),
            preserve_default=False,
        ),
    ]
