# Generated by Django 2.2.7 on 2020-01-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200109_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
