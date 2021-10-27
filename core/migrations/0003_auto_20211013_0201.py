# Generated by Django 3.2.8 on 2021-10-13 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_web3user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='web3user',
            name='is_creator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='web3user',
            name='nonce',
            field=models.CharField(default=1234, max_length=64),
            preserve_default=False,
        ),
    ]
