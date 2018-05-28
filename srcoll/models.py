from django.db import models

# Create your models here.
class Srcoll(models.Model):
    id = models.CharField(primary_key=True,max_length=32)
    desc_remark = models.CharField(max_length=4000)
    status = models.CharField(max_length=1)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tb_srcoll'  # 自定义表名称
