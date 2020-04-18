from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField('标题', max_length=50)
    href = models.URLField('链接')
    status = models.PositiveIntegerField('状态', choices=STATUS_ITEMS, default=STATUS_NORMAL)
    weight = models.PositiveIntegerField('权重', default=1, choices=zip(range(1, 6), range(1, 6)), help_text='权重高展示顺序靠前')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '友链'


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '正常'),
        (STATUS_HIDE, '删除'),
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )
    title = models.CharField('标题', max_length=50)
    display_type = models.PositiveIntegerField('展示类型', default=1, choices=SIDE_TYPE)
    content = models.CharField('内容', max_length=500, blank=True, help_text='如果设置的不是HTML类型，可为空')
    status = models.PositiveIntegerField('状态', choices=STATUS_ITEMS, default=STATUS_SHOW)
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'
