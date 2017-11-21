from django.conf.urls import url, include
# from django.contrib import admin
import xadmin
from post import views

from django.views.static import serve   # 媒体文件
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^post/home/', views.home),
    url(r'^post/show/', views.show),
    url(r'^post/edit/', views.edit),
    url(r'^post/search/', views.search),
    url(r'^post/comment/', views.comment),
    url(r'^post/new_post', views.new_post, name='new_post'),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^operation/', include('operation.urls', namespace='operation')),
    # 配置url
    url(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # 验证码
    url(r'^captcha/', include('captcha.urls')),
]
