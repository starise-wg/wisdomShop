# Generated by Django 2.1.5 on 2020-03-03 07:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('zhylbwg', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='address',
            new_name='userAddress',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='age',
            new_name='userAge',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='name',
            new_name='userName',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='pwd',
            new_name='userPwd',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='telphone',
            new_name='userTelphone',
        ),
    ]