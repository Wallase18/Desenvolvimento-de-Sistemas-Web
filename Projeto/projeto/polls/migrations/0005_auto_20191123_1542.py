# Generated by Django 2.2.4 on 2019-11-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20191123_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
