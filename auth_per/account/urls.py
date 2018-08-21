from django.conf.urls import url
from account import views

app_name = 'permission'

urlpatterns = [
    url(r'^login/$', views.user_login),
    url(r'^detail/$', views.detail_log),
    url(r'^add/$', views.add_log),
    url(r'^delete/$', views.delete_log),
    url(r'^update/$', views.update_log),
    url(r'^share/$', views.share_log),
    url(r'^attendance/$', views.attendance),
    url(r'^logout/$', views.user_logout),
]