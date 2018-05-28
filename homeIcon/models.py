from django.db import models

# Create your models here.
class HomeIcon(models.Model):
    id = models.CharField(primary_key=True,max_length=32)
    c_index = models.IntegerField(max_length=3)
    status = models.CharField(max_length=1)
    icon = models.DateTimeField(max_length=256)
    class Meta:
        db_table = 'tb_home_icon'  # 自定义表名称