# Generated by Django 2.2.4 on 2019-11-21 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('Descricoa', models.CharField(max_length=200)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
    ]
