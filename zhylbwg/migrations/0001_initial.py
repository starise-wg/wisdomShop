# Generated by Django 2.1.5 on 2020-03-10 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50, unique=True, verbose_name='品牌名称')),
                ('brand_pic', models.ImageField(max_length=50, upload_to='', verbose_name='品牌logo')),
                ('brand_company', models.CharField(max_length=50, verbose_name='品牌所属公司')),
            ],
        ),
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
                ('host_ip', models.CharField(max_length=20)),
                ('hostgroup', models.ForeignKey(on_delete='CASCADE', to='zhylbwg.hostgroup')),
            ],
            options={
                'verbose_name': '主机信息',
                'verbose_name_plural': '主机信息',
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True, verbose_name='产品名称')),
                ('product_code', models.CharField(max_length=50, verbose_name='产品编码')),
                ('product_pic', models.CharField(max_length=1000, verbose_name='产品图片')),
                ('product_introduction', models.CharField(max_length=50, verbose_name='产品简介')),
                ('product_details', models.CharField(max_length=50, verbose_name='产品详情')),
                ('product_price',
                 models.DecimalField(decimal_places=1, max_digits=6, max_length=50, verbose_name='产品价格')),
                ('product_brand_id',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zhylbwg.BrandName',
                                   to_field='brand_name', verbose_name='产品品牌')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=10)),
                ('userPwd', models.CharField(max_length=100)),
                ('userTelphone', models.CharField(max_length=10)),
                ('userAddress', models.CharField(max_length=10)),
                ('userAge', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfoMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(choices=[(1, '普通用户'), (2, 'VIP'), (3, 'SVIP')])),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64)),
                ('user',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='zhylbwg.UserInfoMessage')),
            ],
        ),
    ]
