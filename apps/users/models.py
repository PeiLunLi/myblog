from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from post.models import Article


class UserPro(AbstractUser):
    '''用户扩展表'''
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=6,choices=(('male', "男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 设置默认头像和上传头像的路径
    image = models.ImageField(upload_to="image/%Y%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = verbose_name_plural = "用户信息"

    def __str__(self):
        return self.username

    def getArticle(self):
        '''
        获取文章
        :return:
        '''
        all_Articles =Article.objects.filter(uid =self.id)
        return all_Articles
    def get_articles_nums(self):
        """
        获取文章数量
        """
        all_article = Article.objects.filter(aid=self.id).all()
        return all_article.count()

    get_articles_nums.short_description = "文章数"
