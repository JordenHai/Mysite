from django.db import models

# Create your models here.
# app01_userinfo
# 字符串、时间、数字、二进制
'''
字段的参数：
null               -> db是否可以为空
default            -> 默认值
primary_key        -> 主键
db_column          -> 列名
db_index           -> 索引
unique			   -> 唯一索引
unique_for_date    -> 
unique_for_month
unique_for_year
auto_now           -> 创建时，自动生成时间
auto_now_add       -> 更新时，自动更新为当前时间
'''
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    # email    = models.CharField(max_length=64)
    # test     = models.URLField(max_length=256)



class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)

