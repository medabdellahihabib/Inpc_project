# Generated by Django 4.2.7 on 2023-12-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirstapp', '0004_rename_point_price_point_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='famille_produit',
            new_name='famille_produit_ID',
        ),
        migrations.AlterField(
            model_name='produit',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]