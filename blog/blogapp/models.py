from django.db import models


class Aritcle(models.Model):
    #创建文章标题模型
    handline = models.CharField(null=True,blank=True,max_length=500)
    #创建文章模型
    content = models.TextField(null=True,blank=True)
    hand_img = models.ImageField(upload_to="upload",null = False,blank=True)
    #传递参数实现文章分类
    TAG_CHOICES = (
        ('网站开发','网站开发'),
        ('随笔、行记','随笔、行记'),
    )
    tag = models.CharField(null=True,blank=True,max_length=5,choices=TAG_CHOICES)
    #返回参数为文章标题
    def __str__(self):
        return self.handline

class Comment(models.Model):
    #创建评论模型的用户名
    name = models.CharField(null=True,blank=True,max_length=500)
    #创建评论模型的评论
    comment = models.TextField()
    belong_to = models.ForeignKey(to=Aritcle,related_name='under_comments',null=True,blank=True)
    def __str__(self):
        return self.comment