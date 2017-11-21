__author__ = 'Pillar.Li'
import xadmin
from xadmin import views
from .models import UserPro

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class UserProAdmin(object):
    list_display = ['nick_name', 'birthday', 'gender', 'address','mobile','get_articles_nums']
    search_fields = ['nick_name', 'birthday', 'gender', 'address','mobile','get_articles_nums']

# xadmin.site.register(UserPro,UserProAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)