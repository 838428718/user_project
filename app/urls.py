from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^show_item', views.show_item, name='show_item'),
    url(r'^delete_user', views.delete_user, name='delete_user'),
    url(r'^edit_user', views.edit_user, name='edit_user'),
    url(r'^show_user_info', views.show_user_info, name='show_user_info')
]