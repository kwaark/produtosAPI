# Generated by Django 4.1.2 on 2022-10-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_produto_codigo_de_barras_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo_de_barras',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='codigo_interno',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
