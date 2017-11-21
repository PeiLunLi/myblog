from django.db import models


class Article(models.Model):
    uid = models.IntegerField(default=0, verbose_name='关联')  # Article_id 做关联
    title = models.CharField(max_length=128,verbose_name='标题',help_text='标题')
    date = models.DateTimeField(auto_now_add=True,verbose_name='日期',help_text='日期')
    content = models.TextField(verbose_name='正文',help_text='正文')
    def get_comments(self):
        '''
        获取评论
        :return:
        '''
        comments = Comment.objects.filter(aid=self.id)
        return comments

    def get_comments_nums(self):
        """
        获取评论数量
        """
        all_lessons = Comment.objects.filter(aid=self.id).all()
        return all_lessons.count()

    get_comments_nums.short_description = "评论数"


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural =verbose_name='文章表'


class Comment(models.Model):
    aid = models.IntegerField(default=0, verbose_name='关联')
    name = models.CharField(max_length=128,verbose_name='名字')
    date = models.DateTimeField(auto_now_add=True,verbose_name='日期')
    content = models.TextField(verbose_name='评论内容')
    def __str__(self):
        return self.content
    class Meta:
        verbose_name_plural =verbose_name='评论表'

