# Generated by Django 4.1.5 on 2023-01-27 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bank", "0003_alter_bank_cpf_alter_bank_valor"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bank",
            old_name="cartão",
            new_name="cartao",
        ),
    ]
