from django.contrib import admin

# Register your models here.
from .models import Grades,Students
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
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
class StudentsAdmin(admin.ModelAdmin):
    def isdeleteinfo (self):
        '''数据表中的bool值显示问题'''
        if self.isdelete:
            return '是'
        else:
            return '否'
    isdeleteinfo.short_description = '是否删除'
    list_display = ['pk','sname','sage','scontend',isdeleteinfo,'sgrade_id']
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 10
    fields = ['sname','sage','scontend','isdelete','sgrade']
    actions_on_top = False
    actions_on_bottom = True
    #执行动作在页面中的展示位置
admin.site.register(Students,StudentsAdmin)