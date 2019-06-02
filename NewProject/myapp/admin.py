from django.contrib import admin

# Register your models here.
from .models import Grades,Students
class GradesAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','isDelete']#显示字段
    list_filter = ['gname']#过滤字段
    search_fields = ['gname']#搜索字段
    list_per_page = 5 #分页数据量
    # #添加修改页属性
    # fields = ['ggirlnum','gboynum','gname','gdate','isDelete']#规定属性的先后顺序
    fieldsets = [('num',{"fields":['ggirlnum','gboynum']}),
                  ('base',{'fields':['gname','gdate','isDelete']})]#分页
    #fields 和 fieldsets 不能同时存在
admin.site.register(Grades,GradesAdmin)
admin.site.register(Students)