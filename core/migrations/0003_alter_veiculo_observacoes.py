# Generated by Django 4.1.6 on 2023-02-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_veiculo_proprietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]