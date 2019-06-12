from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'(\d+)/$',views.detail),
    url('我喜欢你',views.love),
    # 括号中的数字作为参数传给 detail 函数

    url(r'^grades/$',views.grades),
]