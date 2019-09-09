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
unique_for_month   ->
unique_for_year    ->

auto_now           -> 创建时，自动生成时间
auto_now_add       -> 更新时，自动更新为当前时间
'''
"""
choices			  -> django admin中显示下拉框，避免连表查询
blank             -> django admin是否可以为空
verbose_name      -> django admin显示字段中文
editable          -> django admin是否可以被编辑
error_messages    -> 错误信息欠
help_text         -> django admin提示
validators		  -> django form ,自定义错误信息（欠）
"""
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    user_type_choices = (
        (1, '超级用户'),
        (2, 'web用户'),
        (3, 'docker用户'),
        (4, 'ngix用户'),
        (5, '一般用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices, default=5)
    # email    = models.CharField(max_length=64)
    # test     = models.URLField(max_length=256)

class UserGroup(models.Model):
    uid     = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,null=True)
    ctime   = models.DateTimeField(auto_now=True,null=True)
    uptime  = models.DateTimeField(auto_now=True,null=True)
    user_type_choices = (
        (1, '超级用户'),
        (2, 'web用户'),
        (3, 'docker用户'),
        (4, 'ngix用户'),
        (5, '一般用户'),
    )
    user_type_id = models.IntegerField(choices=user_type_choices,default=5)
    """
    # obj = UserGroup.objects.filter(id=1).update(caption='CEO') 此条不会对uptime生效
    # obj = UserGroup.objects.filter(id=1).first()
    # obj.caption = "CEO"
    # obj.save()
    """