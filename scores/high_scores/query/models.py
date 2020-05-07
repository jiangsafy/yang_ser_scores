from django.db import models

# Create your models here.
from django.db.models import Model
from django.utils import timezone

#
class Hign_scores(Model):
    client_name = models.CharField(verbose_name='客户端名称', max_length=100)
    fraction = models.IntegerField(verbose_name='玩家分数', default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    update_time = models.DateTimeField(verbose_name="更新时间", default=timezone.now)
#
    class Meta:
        db_table = 'hign_scores'
        verbose_name = '玩家排名'
        verbose_name_plural = verbose_name
    def __str__(self):
        return f"客户端名字:{self.client_name},用户分数:{self.fraction}"
