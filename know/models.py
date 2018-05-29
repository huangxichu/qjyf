from django.db import models

class Know(models.Model):
    id = models.CharField(primary_key=True,max_length=36)
    title = models.CharField(max_length=256)
    icon = models.CharField(max_length=256)
    status = models.CharField(max_length=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_know'  # 自定义表名称

class KnowDetail(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    know_id = models.CharField(max_length=36)
    type = models.CharField(max_length=1)
    icon = models.CharField(max_length=256)
    c_index = models.IntegerField(max_length=3)
    context = models.CharField(max_length=4000)

    class Meta:
        db_table = 'tb_know_detail'  # 自定义表名称
