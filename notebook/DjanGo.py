                              DjanGo

1.[坑·1]django下载完之后要配置环境变量（人已经麻了）
   放一下环境变量配置：
   D:\Sequence\python\Scripts
   D:\Sequence\python\Lib\site-packages\django

2.新建项目侯settings.py文件中 ALLOWED_HOSTS 代表允许哪些人访问
  改为 ALLOWED_HOSTS=["*"]就能让所有人都访问
3.SQLite：轻量级的嵌入式的数据库
   特点是小
   常用场景：Android·ios·wp
   常规操作百分之九十五和mysql一样
4.还是上面那个文件，AUTH_PASSWORD_VALIDATORS：系统认证器
5.语言配置：LANGUAGE_CODE = 'en-us'(英语)
                          = 'zh-hans'(中文)
6.时间配置：TIME_ZONE = 'Asia/Shanghai'
7.万能键alt+enter
8.实现一个请求
   8.1 urls.py中添加 path(参数，视图函数),
       views.py中添加自定义函数

       如：from App import views
           path('hello',views.hello), #注：方法调用不要加括号
           
           from django.shortcuts import HttpResponse
           def hello(request):
               return HttpResponse("*****")
      
   8.2 views中的第一个参数是requset不变的
       永远要记得返回response（也可能返回response子类）

9. heml快捷键 tabtab
   ul>li
   ul*5
   ul>li*5

10.返回一个网页
   新建一个空目录命名为templates
   10.1在其中新建html文件（这里命名为index）
   10.2在urls中添加
       path('index/',views.index),
   10.3在views中添加
       def index(request):
           return render(request,'index.html')
       #request固定，第二个填模板名
   10.4在settings.py中INSTALLED_APPS添加
       'App',


11.所有人都可以访问：
   python manage.py runserver 0.0.0.0:8000

12.补充一下新建项目...
   进入到djabgo-admin所在的文件夹
   输入 django-admin startproject 文件名 进行新建文件
   (当然 配置完环境变量后就不需要进入所在文件夹了)
   进入到manage.py所在的目录，
   输入 python manage.py startapp App #就按App的规则来命名

13.在App中注册一个templates后，在总目录下又新建一个templates
   此时运行出网页会有bug，需要在settings.py文件中，找到TEMPLATES
   找到'DIRS':[]
   在其中添加[os.path.join(BASE_DIR,'templates'),]
   #base_dir代表当前的工程路径，后边加一个templates
   #os那句总体代表templates的相对路径，当然可以右键copy path的绝对路径
   #直接'放绝对路径'
   建议直接写相对路径
   建议在总目录下创建模板文件夹

14.App可以有多个，不是只能有一个，记得每创建完一个就在INSTALED_APPS中添加
   比如我再创建一个two，这时我还可以在原来的地方继续写路由（urls）
   但是更建议的是，在two的文件下新建一个urls.py
   在里面写 urlpatterns=[]#切记，它是一个列表
   urlpatterns=[
              url('index/',views.index),
           ]
   此时这个还没有导包，直接用alt+enter
   注意：导的是：from django.conf.urls import url
   以及 from two import views

   让主路由知道还有一个子路由，需要在主路由中添加子路由的路径
   from django.urls import path,include
   path('two/',include('Two.urls')),

15.-项目如果过于复杂，可以进行拆分
   -拆分为多个app
   -继续拆分路由器
      ·在app中创建自己的urls
         urlpatterns 路由规则列表
         在根urls中进行子路由的包含
      ·子路由使用
         根路由规则+子路由规则

16.models使用了ORM技术
   Object Relational Mapping  对象关系映射
   将业务逻辑进行了一个解耦合
     object.save()
     object.delete()
     不管是mysql还是什么，都可以这样
   关系型数据库
     DDL(定义数据库)
       jango通过models定义实现数据库定义

17.数据库连接
   如果报连接错误，将database files第一行改成绝对路径
   如下：
      D:\Sequence\python\Scripts\FIRST\db.sqlite3

   17.1在models里继承模型让django承认
       s_name=models.CharField(max_length=16)
       #定义一个字符串类型的变量 规定最大长度为16

   17.2让数据库知道models里面定义了
       1.做数据迁移
         python manage.py makemigrations
       2.映射到库中
         python manage.py migrate

       

       
     
