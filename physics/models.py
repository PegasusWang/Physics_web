from django.db import models


class Student(models.Model):
    """Student Info"""
    stu_id = models.CharField(u'学号', max_length=30, primary_key=True)
    name = models.CharField(u'姓名', max_length=30)
    password = models.CharField(u'密码', max_length=30)
    answer = models.CharField(u'答案', max_length=30)
    email = models.EmailField(u'邮箱', blank=True)

    def __unicode__(self):
        return '{stu_id} {name}'.format(stu_id=self.stu_id, name=self.name)


class Teacher(models.Model):
    """Teacher Info"""
    name = models.CharField(u'姓名', max_length=30)
    email = models.EmailField(u'邮箱', blank=True)

    def __unicode__(self):
        return self.name


class Questoin(models.Model):
    """Question Info"""
    title = models.TextField(u'题目')
    content = models.TextField(u'选项')
    answer = models.CharField(u'答案', max_length=1)
    a_select_users = models.IntegerField(u'选A')
    b_select_users = models.IntegerField(u'选B')
    c_select_users = models.IntegerField(u'选C')
    d_select_users = models.IntegerField(u'选D')

    def __unicode__(self):
        return self.title


class Notification(self):
    """Notification Info"""
    owener = models.ForeignKey(Teacher)
    title = models.TextField(u'通知标题')
    content = models.TextField(u'通知内容')
    time = models.DateField(u'通知时间')

    def __unicode__(self):
        return self.title
