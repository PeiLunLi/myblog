from django.conf.urls import url
from users import views
urlpatterns = [
    # url(r'^$', views.home),
    url(r'^login/', views.User_login,name='login'),
url(r'^logoff/', views.logoff,name='logoff'),
url(r'^register/', views.register,name='register'),

]