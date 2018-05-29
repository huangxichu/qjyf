from django.db import models

class HomeIcon(models.Model):
    id = models.CharField(primary_key=True,max_length=36)
    c_index = models.IntegerField(max_length=3)
    status = models.CharField(max_length=1)
    icon = models.CharField(max_length=256)

    class Meta:
        db_table = 'tb_home_icon'  # 自定义表名称