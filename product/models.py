from django.db import models

# Create your models here.

class ProductBase(models.Model):
    id = models.CharField(primary_key=True,max_length=36)
    name = models.CharField(max_length=256)
    desc_remark = models.CharField(max_length=4000)
    icon = models.CharField(max_length=256)
    status = models.CharField(max_length=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_production_base'  # 自定义表名称
