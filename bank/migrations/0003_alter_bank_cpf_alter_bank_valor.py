# Generated by Django 4.1.5 on 2023-01-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank", "0002_alter_bank_cartão_alter_bank_valor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bank",
            name="cpf",
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name="bank",
            name="valor",
            field=models.IntegerField(),
        ),
    ]
