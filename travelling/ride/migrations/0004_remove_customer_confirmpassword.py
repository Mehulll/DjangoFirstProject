# Generated by Django 2.2.3 on 2019-09-26 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0003_auto_20190925_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='confirmpassword',
        ),
    ]
