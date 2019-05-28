# 基本操作

## 	设计表结构

### 		班级表结构

#### 			表名：

##### 					grade

#### 			字段:

##### 					班级名称  gname

##### 					成立时间  gdate

##### 					女生总数  ggirlnum

##### 					男生总数  gboy num

##### 					是否删除  isdelete

### 		学生表结构

#### 			表名:students

#### 			字段

​					学生姓名

​					学生性别

​					学生年龄

## 	配置数据库

### 		**注意：Django 默认使用的是 SQLite 数据**

​			在 setting.py 文件中，通过 DATABASES 选项进行数据库配置

​			1：在 init,py 中写入 

```python
import pymysql
pymysql.install_as_MySQLdb()
```

​			2:	在 setting.py 中把 ENGINE 中的sqllite换成mysql

​					name中放入配置好的数据库名

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "sunck",#数据库名
        'USER':'root',#用户名
        'PASSWORD':'123456',#密码
        "HOST":'localhost',#服务器ip
        'PORT':'3306',#端口
    }
}
```

## 	创建应用

​		在一个项目中，可以创建多个应用，每个应用惊醒一种业务处理。

​		打开command，进入我们的项目下的project, **执行<python manage.py startapp myapp>**

```
C:\Users\Administrator\Desktop\Django_Project_test\project
```

#### 		目录说明

​			admin.py : 站点配置

​			models.py  模型

​			view.py       视图

## 	激活应用

### 在 setting.py 中将 myapp 应用加入到INSTALLED_APPS中

## 定义模型

一个数据表就对应一个模型

在 models.py 中定义模型

在 myapp 中 model.py中

```python
from django.db import models

# Create your models here.
#班级
class Grades(models.Model):
    gname = models.CharField(max_length =20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
#学生
class Student(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isdelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey('Grade',on_delete=models.CASCADE)
```

创建相应模型类

**说明**

1：不需要定义主键，声称是会自动添加，并且值为自动自动增加的

## 生成数据表

在数据库中生成 数据表

1：生成迁移文件

在project中执行 manger.py 

```
python manager.py makemigrationss
#在 migrations 目录下生成一个迁移文件，此时数据库中还没有身材高恒数据表
```

2：执行迁移

```
python manage.py migrate
```

```
#cmd执行命令
C:\Users\Administrator\Desktop\Django_Project_test>cd NewProject

C:\Users\Administrator\Desktop\Django_Project_test\NewProject>python manage.py startapp myapp

C:\Users\Administrator\Desktop\Django_Project_test\NewProject>python manage.py makemigrations
Traceback (most recent call last):
  File "manage.py", line 15, in <module>
    execute_from_command_line(sys.argv)
  File "E:\ProgramData\Anaconda3\lib\site-packages\django\core\management\__init__.py", line 381, in execute_from_command_line
    utility.execute()
  File "E:\ProgramData\Anaconda3\lib\site-packages\django\core\management\__init__.py", line 357, in execute
    django.setup()
  File "E:\ProgramData\Anaconda3\lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "E:\ProgramData\Anaconda3\lib\site-packages\django\apps\registry.py", line 112, in populate
    app_config.import_models()
  File "E:\ProgramData\Anaconda3\lib\site-packages\django\apps\config.py", line 198, in import_models
    self.models_module = import_module(models_module_name)
  File "E:\ProgramData\Anaconda3\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\Administrator\Desktop\Django_Project_test\NewProject\myapp\models.py", line 12, in <module>
    class Student(models.Model):
  File "C:\Users\Administrator\Desktop\Django_Project_test\NewProject\myapp\models.py", line 19, in Student
    sgrade = models.ForeignKey('Grade')
TypeError: __init__() missing 1 required positional argument: 'on_delete'

C:\Users\Administrator\Desktop\Django_Project_test\NewProject>python manage.py makemigrations
SystemCheckError: System check identified some issues:

ERRORS:
myapp.Student.sgrade: (fields.E300) Field defines a relation with model 'Grade', which is either not installed, or is abstract.
myapp.Student.sgrade: (fields.E307) The field myapp.Student.sgrade was declared with a lazy reference to 'myapp.grade', but app 'myapp' doesn't provide model 'grade'.

C:\Users\Administrator\Desktop\Django_Project_test\NewProject>python manage.py makemigrations
Migrations for 'myapp':
  myapp\migrations\0001_initial.py
    - Create model Grades
    - Create model Student

C:\Users\Administrator\Desktop\Django_Project_test\NewProject>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myapp, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying myapp.0001_initial... OK
  Applying sessions.0001_initial... OK

C:\Users\Administrator\Desktop\Django_Project_test\NewProject>
```

