#-*- coding: utf-8 -*-

from django.db import models

class Hostinfromation(models.Model):
    # 定义主机相关信息字段
    host_name = models.CharField(max_length=30)
    # host_ip = models.GenericIPAddressField(max_length=40)
    host_ip=models.CharField(max_length=20)
    # 定义主机外键
    # 在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题
    """
        on_delete有CASCADE、PROTECT、SET_NULL、SET_DEFAULT、SET()五个可选择的值
        CASCADE：此值设置，是级联删除。
        PROTECT：此值设置，是会报完整性错误。
        SET_NULL：此值设置，会把外键设置为null，前提是允许为null。
        SET_DEFAULT：此值设置，会把设置为外键的默认值。
        SET()：此值设置，会调用外面的值，可以是一个函数。
        一般情况下使用CASCADE就可以了。
    """
    hostgroup = models.ForeignKey('hostgroup',on_delete='CASCADE')
    class Meta:
        verbose_name = '主机信息'
        verbose_name_plural = '主机信息'
        app_label = 'zhylbwg'
    def __unicode__(self):
        return self.host_name
class hostgroup(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        app_label = 'zhylbwg'
    def __unicode__(self):
        return self.name