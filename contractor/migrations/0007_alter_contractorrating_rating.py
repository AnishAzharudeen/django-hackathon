# Generated by Django 4.2.18 on 2025-02-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0006_contractorrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractorrating',
            name='rating',
            field=models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')], default=1),
        ),
    ]
