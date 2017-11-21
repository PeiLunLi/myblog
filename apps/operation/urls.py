from django.conf.urls import url
from operation import views


urlpatterns = [
url(r'^active/(?P<active_code>.*)/$',views.ActiveUser ,name='user_active'),
        ]