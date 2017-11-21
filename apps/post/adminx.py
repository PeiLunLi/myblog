import xadmin
from .models import Article,Comment
from xadmin import views



class ArticleAdmin(object):
    list_display =['title','date','content','get_comments_nums']
    search_fields =['title','date','content','get_comments_nums']


class CommentAdmin(object):
    list_display =['name','date','content']
    search_fields =['name','date','content']




xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Comment,CommentAdmin)