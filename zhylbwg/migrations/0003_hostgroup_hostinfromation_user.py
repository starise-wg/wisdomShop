# Generated by Django 2.1.5 on 2019-01-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zhylbwg', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='hostgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hostinfromation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=30)),
                ('host_ip', models.GenericIPAddressField()),
                ('host_group', models.ForeignKey(on_delete='CASCADE', to='zhylbwg.hostgroup')),
            ],
            options={
                'verbose_name': '主机信息',
                'verbose_name_plural': '主机信息',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
