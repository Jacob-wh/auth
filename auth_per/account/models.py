from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.


class AccessControl(models.Model):
    """
    自定义权限控制
    """
    class Meta:
        # 分为两个角色管理员和普通用户
        # 管理员可以对日志增删改查，普通用户可以查看日志和签到
        permissions = (
            ('add_log', u'add'),
            ('detail_log', u'detail'),
            ('delete_log', u'delete'),
            ('update_log', u'update'),
            ('share_log', u'share'),
            ('attendance', u'attendance'),
        )


class Menu(models.Model):
    """
    菜单模块
    """
    pid = models.ForeignKey('Menu', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('菜单名', max_length=20, null=False)
    url = models.CharField('菜单路由', max_length=50, null=False)
    display = models.BooleanField('是否显示', default=False)
    sort = models.IntegerField('排序', default=0)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name="menu")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    sex = models.CharField(verbose_name='性别', max_length=5, null=False, db_index=True, blank=False)
    age = models.IntegerField(verbose_name='年龄', null=False, db_index=True)
