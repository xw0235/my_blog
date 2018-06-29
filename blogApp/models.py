from django.db import models

from DjangoUeditor.models import UEditorField


class Category1(models.Model):
    category_1 = models.CharField(
        max_length=32, db_index=True, unique=True, help_text="种类1")
    add_time = models.DateTimeField(auto_now_add=True, help_text="添加时间")

    def __str__(self):
        return self.category_1

    # 按时间降序排列
    class Meta:
        ordering = ['-add_time']


class Category2(models.Model):
    category_2 = models.CharField(
        max_length=32, db_index=True, unique=True, help_text="种类2")
    add_time = models.DateTimeField(auto_now_add=True, help_text="添加时间")

    def __str__(self):
        return self.category_2

    # 按时间降序排列
    class Meta:
        ordering = ['-add_time']


# 标签类
class Tag(models.Model):
    tag = models.CharField(max_length=32, db_index=True,
                           unique=True, help_text="文章标签")
    add_time = models.DateTimeField(auto_now_add=True, help_text="添加时间")

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['-add_time']


# 博客类
class Blog(models.Model):
    title = models.CharField(u'标题', max_length=124, help_text="文章标题")
    head_pic_url = models.CharField(
        u'头图链接', max_length=256, default='/static/img/default.jpg', help_text="主页头图")
    pub_time = models.DateTimeField(auto_now_add=True, help_text="发布时间")
    brief = models.CharField(u'摘要', max_length=256,
                             blank=True, null=True, help_text="文章摘要")
    content = UEditorField(
        u'正文', width=900, height=600, toolbars="full", imagePath="", settings={}, help_text="博客正文")
    page_views = models.PositiveIntegerField(
        u'访问量', default=0, editable=False, help_text="博客访问量")
    category1 = models.ForeignKey(Category1, verbose_name=u'一级目录',)
    category2 = models.ForeignKey(Category2, verbose_name=u'二级目录', null=True)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']


class Profile(models.Model):
    title = models.CharField(u'标题', max_length=124, help_text="博客标题")
    head_pic_url = models.CharField(
        u'头图链接', max_length=256, default='/static/img/default.jpg', help_text="主页头图")
    pub_time = models.DateTimeField(auto_now_add=True, help_text="发布时间")
    brief = models.CharField(u'摘要', max_length=256,
                             blank=True, null=True, help_text="文章摘要")
    content = UEditorField(u'正文', width=900, height=600,
                           toolbars="full", imagePath="", settings={}, help_text="博客正文")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_time']


class Friend_Tags(models.Model):
    tag = models.CharField(max_length=32, db_index=True,
                           unique=True, help_text="好友标签")
    add_time = models.DateTimeField(auto_now_add=True, help_text="添加时间")

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['-add_time']


class Friend(models.Model):
    name = models.CharField(max_length=64, db_index=True,
                            unique=True, help_text="友情链接名称")
    friend_url = models.CharField(u'链接', max_length=256, default='http://')
    tag = models.ManyToManyField(Friend_Tags, blank=True, verbose_name=u'标签')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
