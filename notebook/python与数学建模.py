 
                              python与数学建模


1.数据类型：整数，浮点数，布尔值，空值
2.字符串，用引号来定义，单引号双引号是等价的
  a='hello world' 和a="hellw world"
  
  2.1）三引号用来输入包含多行文字的字符串
      s='''hello
        my
        world'''

  2.2）字符串加法
      s="hello"+"world"

  2.3）字符串的索引
      索引号与c++相同是从0开始的
      s[索引号]
      s[0]

  2.4）字符串的分割
      s="hello world"
      默认是按照空格来分割的
      s.split()
      ['hello','world']

      2.4.1)自定义分隔符：
          s.split(',')

  2.5）查看字符串长度
      len(字符串)
      len(s)

3.基本运算
  3.1）**幂运算，返回x的y次幂
  3.2）//取整除 返回商的整数部分（向下取整）

4.逻辑运算
  4.1）and ：x and y 布尔"与"，如果x为false，则x and y 返回false，否则返回y的值
  4.2）or：x or y 布尔"或"，如果x为非0，它返回x的值，否则返回y的值
  4.3）not x：布尔"非"，如果x为true，返回false。如果x为false，它返回true


5.数据结构
  5.1）列表List，用[]生成，也可以用list
       如list('abcde')

       5.1.1)列表相加
             a=[1,2,3,4,5]
             actor=['s', 'd', 'n', 'f']
             a+actor
             Out[20]: [1, 2, 3, 4, 5, 's', 'd', 'n', 'f']

       5.1.2)列表取值
             a[索引号]#从零开始
             如a[0]=1

       5.1.3)列表追加
             a.append(6)
             out:[1,2,3,4,5,6]

       5.1.4)列表插入
             a.insert(索引号,值)
             a.insert(1,10)
             out:[1,10,2,3,4,5,6]

       5.1.5)元素删除
             a.pop()#删除最末尾的
             a.pop(1)#删除索引号为1的数据元素
                     #索引号依旧从0开始
                     
       5.1.6）切片
             此时a=[1,2,3,4,5]
             1.6.1）a[0:3]#左闭右开区间，对于a而言取了1，2，3

             1.6.2）也可以a[:3]#默认从左边第一个元素开始提取，结果同上

             1.6.3）a[0:]#冒号右边不写，默认取到最后一个元素
                         #对a而言取了所有
                      
             1.6.4）a[0:-1]#取到倒数最后一位的前一位
                           #结果是[1,2,3,4]
                           
             1.6.5)b=[1,2,3,4,5,6,7,8,9,10]
                   b[a:b:i]#从a取到b，但是不包含b，以间隔i为步长进行取值
                   b=[1,2,3,4,5,6,7,8,9,10]
                   b[2:9:3]
                   Out[2]: [3, 6, 9]#写负数从后往前取值

            
  5.2）元组tuple，用()表示，和list相似，但是tuple一旦被初始化就不能修改

  5.3）字典dict，用{key:value}生成dictionary，里面数据可以是任何类型，包括字典
             mv={'name':'肖申克的救赎', 'actor':'罗宾斯', 'score':9.6 ,'country':'USA'}
             3.1）查询
                  mv['name']
                  out:'肖申克的救赎'
             3.2）键查询
                  mv.keys()
                  out:dict_keys(['name', 'actor', 'score'])
             3.4）值查询
                  mv.value()
                  out:dict_values(['肖申克的救赎', 'robins', 9.6])
             3.5）全部查询
                  mv.items()
                  dict_items([('name', '肖申克的救赎'), ('actor', 'robins'), ('score', 9.6)])

             3.6）修改
                  mv['name']='泰坦尼克号'
              
             3.7）添加
                  mv['director']='德拉邦特'

             3.8）删除
                  mv.pop('director')#索引是键


  5.4）集合set，用{}来生成集合，集合中不含有相同元素
       #集合中不能含有任何相同元素，集合用{}表示
       可以用 len() 进行查看
       添加用 add()

       4.1）交集
               s={2,3,4,5}
               s1={1,2,3,4}
               s&s1
       Out[11]: {2, 3, 4}

       4.2）并集
               s|s1
       Out[12]: {1, 2, 3, 4, 5}

       4.3）做差
            s-s1 #属于s但是不属于s1的一些元素


6.可变对象与不可变对象
     
  6.1）可变对象可以对其进行插入、删除等操作，不可变对象不可以对其进行有改变的操作
       python中列表，字典，集合等都是可变的，元组，字符串，整型等都是不可变的 


7.类型转换
  int(3.14)
  3
  float(3)
  3.0

  查看变量类型
  s='adffsa'
  type(s)
  str

8.判断和循环  

  8.1）2==2     True
       3=='a'   False
       'a'=='A' False 
       #python中区分大小写

  8.2）if 2>1:
           print('hellow')

       判断语句

  8.3）a=1
       b=2
       if a>b:
           print('a>b')
       else:    
           print('a<=b')
    
       out:a<=b
  
  8.4）x=0
       if x>0:
           print('x>0')
       elif x==0:
           print('x=0')
       else:
           print('x<0')

  8.5）循环
      8.5.1）for 循环
             for i in [1,2,3,4,5,6,7,8,9]
                 print(i)
             在范围内进行循环
      
      8.5.2）while 循环
             while i<10:
                 print(i)
                 i=i+1

  8.6）列表生成式
       即List Comprehensions，是python内置的非常简单却强大的可以用来创建list的生成式
       list(range(1,11))  #range(1,11)左闭右开区间
       out:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

       [x**2 for x in range(1,10)]
       out:[1, 4, 9, 16, 25, 36, 49, 64, 81]
       
       进行条件判断
       [i for i in range(1,100) if i%10==0]
       out:[10, 20, 30, 40, 50, 60, 70, 80, 90]
       
       转化
       [str(x) for x in range(1,10)]
       ['1', '2', '3', '4', '5', '6', '7', '8', '9']

       转成数字
       [int(x) for x in list('123456789')]
       [1, 2, 3, 4, 5, 6, 7, 8, 9]


9.函数
  9.1）常用内置函数  
       abs(-1) #取绝对值

       a=[1,3,-9,10,34]
       max(a)  #找最大值
       min(a)  #找最小值
       sum(a)  #求和

  9.2）自定义函数
       函数function，通常接受输入参数，并有返回值
       特征：
          使用 def 关键字来定义一个函数
          def 后面的是函数的名称，括号中是函数的参数，不同的参数用.隔开
          def func()：形式必须要有，参数可以为空
          使用缩进来划分函数的内容
          return 返回特定的值，如果省略，返回 None

       def add(x,y):
           a=x+y
           return a
       print(add(2,3))
       
       可以给参数默认值

10.导包语句
    10.1 import numpy
    10.2 import numpy as np
    10.3 from numpy import *  #可以不再写前缀.但是不建议去写

11.numpy在数组上的操作
    11.1让列表中每个元素增加1
        11.1.1使用列表生成式：
                a=[1,2,3,4]
                [x+1 for x in a]
              不能使用a+1

        11.1.2 使用numpy
                a=np.array([1,2,3,4])
                a+1
                a*2

    11.2列表相加   
        11.2.1 b=[2,3,4,5]
              此时用a+b实现的是列表的拼接
              使用列表生成式：
                 [x+y for (x,y) in zip(a,b)]
        
        11.2.2使用numpy
                b=np.array([2,3,4,5])
                a+b

    11.3产生数组
        11.3.1从列表产生数组：
          l=[0,1,2,3]
          a=np.array(l)

        11.3.2从列表传入：
          a=np.array([1,2,3,4])

        11.3.3生成全是0的数组：
          a=np.zeros(5)

        11.3.4生成全是1的数组：
          a=np.noes(5,dtype='int')
          #dtype写数据类型
        
        11.3.5用fill方法将数组设为指定值：
          a.fill(5)
          #fill要求列表中每个元素的数据类型是一致的
          对a进行数据类型的更改
          a=a.astype('float')

        11.3.6生成整数序列
          a=np.arange(1,10)
          #左闭右开区间
          第三参数可以写成步长

        11.3.7生成等差序列： 
          a=np.linspace(1,10,21)
          从1到10一共21个数的等差序列
          #非左闭右开区间

        11.3.8生成随机数  
          a=np.random.rand(10)
          #返回0~1之间的十个不同的随机浮点数
          a=np.random.randn(10)
          #返回服从正态分布的随机数
          a=np.random.randint(1,10,10)
          #返回1-10之间十个随机整数
          
    11.4数组属性
        11.4.1查看类型：
            type(a)
        11.4.2查看数组内部数的类型：
            a.dtype
        11.4.3查看形状，会返回一个元组，每个元素代表这一维的元素数目
            a.shape
            np.shape(a)
        11.4.5查看数组里面元素的数目：
            a.size
        11.4.6查看数组的维度：
            a.ndim

    11.5索引与切片
        11.5.1索引第一个元素：
            a=np.array([0,1,2,3])
            #索引号从0开始
            a[0]       0
            修改
            a[0]=10

        11.5.2切片(支持负索引)
            a=np.array([11,12,13,141,15])
            a[1:3]#左闭右开从0开始
            a[1:-2]#从索引号为1的数开始取，取到倒数第二个元素的前一个元素
            a[-4:3]#从倒数第四个元素开始取，取到整数第三
            上面三个值相同
            
12.多维数组
    12.1 二维数组的生成
         a=np.array([[0,1,2,3],[10,11,12,13]])
         实际上传入的是一个以列表为元素的列表
         ·查看形状
           a.shape
           (2,4)#两行四列
         ·查看元素个数
           a.size
         ·查看维度
           a.ndim

    12.2多维数组的索引
         对于二维数组，可以传入两个数字来索引
         如上的a[1,3]
         1是行索引，3是列索引，中间用逗号隔开，从0开始
         可以利用索引进行赋值
         a[1,3]=-1
         
    12.3多维数组的单行索引
         a[1]返回索引号的第一行的内容

    12.4多维数组的切片
        a=np.array([[0,1,2,3,4,5],
                    [10,11,12,14,13,15],
                    [20,21,22,23,24,25],
                    [30,31,32,33,34,35],
                    [40,41,42,43,44,45],
                    [50,51,52,53,54,55]])
        ·得到第一行的第四个和第五个元素
           a[0,3:5]
        ·得到最后两行的最后两列(44,45,54,55) 
           a[4:,4:]
        ·得到第三列(2,12,22,32,42,52)
           a[:,2]

        每一维都支持切片的规则，包括负索引，省略:
            [lower:upper:step]
  
        取出3，5行的奇数列：
           a[2::2,::2]

    12.5花式索引
        切片只支持连续或者等间隔的切片操作，要实现任意位置的操作
      需要使用花式索引fancy slicing
        
        12.5.1一维花式索引
          与range函数类似，我们可以使用arange函数来产生等差数组
          a=np.arange(0,100,10)
          
          花式索引需要指定索引位置:
              index=[1,2,-3]
              y=a[index]
              print(y)
          取的值是第1，2，-3位置上的值

          可以使用布尔数组来花式索引
           mask=np.array([0,2,2,0,0,1,0,0,1,0],dtype=bool)
          mask必须是布尔数组。长度必须和数组长度相等 
           a[mask]
          取出的是位置为true(非0)的数
        
        12.5.2二维花式索引(如12.4的数组)
          ·返回一条次对角线上的5个值(1,12,23,34,45)
            先写行值，再写列值
            a[(0,1,2,3,4),(1,2,3,4,5)]

          ·返回最后三行的1，3，5列
            a[3:,[0,2,4]]
          与切片不同，花式索引返回的是原对象的一个复制而不是引用

     12.6不完全索引
        ·只给定行索引的时候，返回整行：
          y=a[:3]#返回的是前三行
        ·也可以用花式索引引出第2，3，5行:
            con=np.array([0,1,1,0,1,0],dtype=bool)
            a[con]

13. where语句 
   where(array)
   where函数会返回所有非零元素的索引
   
   a=np.array([0,12,5,20])
   判断数组中的元素是不是大于10：
     a>10
     array([False,True,False,True],dtype=bool)
   
   数组中所有大于10的元素的索引位置:
     np.where(a>10)
     (array([1,3],dtype=int64),)

   注意，where的返回值是一个元组，返回的是索引位置，索引[1,3]大于10的数
   也可以直接用数组操作
     a[a>10]
     array([12,20])
     a[np.where(a>10)]

14.类型转换
   可以用a=np.array([1.5,-3],dtype=float)
   也可以用asarray
     14.1 np.asarray(a,dtype=float)

     14.2 astype方法
       a=np.array([1,2,3])
       a.astype(float)
       没有赋值给a，实际上a的值并没有发生改变

15.数组操作
   数据：
   import numpy as np
   mv_name=['肖申克的救赎','控方证人','美丽人生','阿甘正传','霸王别姬','泰坦尼克号','辛德勒的名单','这个杀手不太冷','废物','大佬']
   mv_num=np.array([692795,42995,327855,580987,478523,127074,306904,662552,284652,159302])
   mv_score=np.array([9.6,9.5,9.5,9.4,9.4,9.4,9.4,9.3,9.3,9.3])
   mv_length=np.array([142,116,116,142,171,194,195,133,109,92])
   #电影名、评分人数、评分、电影时长

   15.1 数组排序
     15.1.1 sort函数
       np.sort(mv_num)
       依然没有改动原数组
     
     15.1.2 argsort函数
       返回从小到大的排列在数组中的索引位置
       查看评分最少的电影名称
       order=np.argsort(mv_num)
       mv_name[order[0]]#注意，这里写的是索引位置

   15.2 求和:np.sum(mv_num)或者mv_num.sum()
        最大值:np.max(mv_length)或者mv_length.max()
        最小值:min,
        均值:mean
        标准差:std
        相关系数矩阵:cov(mv_score,mv_length)
        
   15.3 多维数组的操作
      15.3.1 数组形状
        reshape，不会修改原来数组的值，而是返回一个新数组
        a=np.arange(6)
        a.shape=2,3#转成两行三列的二维数组 修改了a的值

      15.3.2 转置：
        a=a.reshape(2,3)
        a.T或者a.transpose()
        注意：没有赋值给a本身，那么a数组本身是不会变化的

   15.4 数组连接：concatenate
        concatenate((a0,a1,...,an),axis=0)
        默认是按照列来进行拼接
        如果是按行来进行拼接，那么需要把axis改成1
        这些数组要用()包括到一个元组中去
        除了给定轴外，其它轴长度必须是一样的

        根据第一维进行连接：
          x=np.array([[0,1,2],[10,11,12]])
          y=np.array([[50,51,52],[60,61,62]])
          z=np.concatenate((x,y))
          z=array([[ 0,  1,  2],
                   [10, 11, 12],
                   [50, 51, 52],
                   [60, 61, 62]])
          相应的可以使用np.vstack((x,y))#堆叠

        根据第二维进行拼接：
          z=np.concatenate((x,y),axis=1)
          z=array([[ 0,  1,  2, 50, 51, 52],
                   [10, 11, 12, 60, 61, 62]])
          相应的可以使用np.hstack((x,y))

        因为x,y形状是一样的，还可以将它们拼接成三维的数组，只是concatenate不提供
          z=np.array((x,y))
          z=array([[[ 0,  1,  2],
                    [10, 11, 12]],
                    
                   [[50, 51, 52],
                    [60, 61, 62]]])
        
        维度的话可以用np.dstack((x,y))

        绝对值：abs
        指数：exp
        中值：media
        累计和：cumsum


16.散点图
   import numpy as np
   import matplotlib.pyplot as plt
   height=[123,214,352,123,234,1231,3]
   weight=[121,432,23,123,43,123,565]
   plt.scatter(height,weight)
   plt.show()
   
   读取scv数据并根据列画出散点图
     import pandas as pd
     iris = pd.read_csv("demand_2016.03.10_510100_.csv")
      #注意：这个路径是添加到项目目录下的文件路径
     plt.scatter(iris.loc[1:,'longitude'],iris.loc[1:,'latitude'])
     plt.show()
      #选取从第2行到最后一行，longitude、latitude列进行绘制

     选取第11，12点时刻的数据
     iris[(iris['hour']==12)|(iris['hour']==11)] 

   外观调整：
     ·点大小：s
        plt.scatter(iris.loc[1:,'longitude'],iris.loc[1:,'latitude'],s=10)
       s是面积不是直径
     ·颜色：c
        c='r'#将颜色改为红色，默认是蓝色的，也就是b
     ·形状：marker  
     ·透明度：alpha

   中文显示x坐标，y坐标，图名
     #-*- coding: utf-8 -*
     import matplotlib as mt
     font ={'family':'MicroSoft YaHei'} #win可以显示中文
     mt.rc("font",**font)
     plt.scatter(iris.loc[1,'传感器经度'],iris.loc[1,'传感器纬度'],c='r')
     plt.scatter(iris.loc[2:,'传感器经度'],iris.loc[2:,'传感器纬度'],c='b')
     plt.xlabel('传感器经度')
     plt.ylabel('传感器纬度')
     plt.title('传感器分布示意图')
     plt.show()


17.折线图
   linespace(-10,10,100)
   #生成等区间的一个数
   #这里是从-10开始到10，平均分成100份
   x=np.linspace(-10,10,100)
   y=x**3
   plt.plot(x,y)
   plt.show()

   绘制带有时间的折线图
     import matplotlib.dates as mdates
     date,open,close=np.load('00001.scv',delimiter=','
             converters={0:mdates.strpdate2num('%m/%d/%y')},
             #1/1/2001 将这样的时间以月/日/年的格式读入
             skiprows=1,usecols=(0,1,4),#读入0，1，4列
             unpack=True)
     plt.plot_date(date,open,'-')
     #-代表线段
    
   参数说明
     ·linestyle:线形
     ·color：颜色
     ·marker：形状
     plt.xticks设置x轴的刻度

18.条形图
   垂直单列条形图
     n=5
     y=[20,10,30,25,15]
     index=[10,15,20,15,30]
     a=[1,2,3,4,5]
     pl=plt.bar(x=index,height=y,width=0.1)
     plt.show()

   横向单列条形图
     n=5
     index=[10,15,20,15,30]
     a=[1,2,3,4,5]
     pl=plt.barh(y=index,height=2,width=a)
     plt.show()

   双列垂直条形图
     index=np.arange(4)
     sales_bj=[52,55,63,53]
     sales_sh=[44,66,55,41]
     bar_width=0.3
     plt.bar(index,sales_bj,bar_width,color='b',label="the first bar")
     plt.bar(index+bar_width,sales_sh,bar_width,color='r',label="the second bar")
     plt.legend(loc='upper left')
     plt.show()
     #左上显示直线含义
   
   单列垂直叠加条形图
     index=np.arange(4)
     sales_bj=[52,55,63,53]
     sales_sh=[44,66,55,41]
     bar_width=0.3
     plt.bar(index,sales_bj,bar_width,color='b',label="the first bar")
     plt.bar(index,sales_sh,bar_width,color='r',label='the second bar',bottom=sales_bj)
     plt.legend(loc='upper left')
     plt.show()

   参数说明
     ·color：颜色
     ·alpha：透明度
     ·edgecolor：图形边缘颜色
     ·legend：loc参数如下:
         'best'         : 0, (only implemented for axes legends)(自适应方式)
         'upper right'  : 1,
         'upper left'   : 2,
         'lower left'   : 3,
         'lower right'  : 4,
         'right'        : 5,
         'center left'  : 6,
         'center right' : 7,
         'lower center' : 8,
         'upper center' : 9,
         'center'       : 10,
     ·linewidth or linewidths or lw：边缘or线的宽    

19.直方图
   mu=100
   sigma=20
   x=mu+sigma*np.random.randn(2000)
   plt.hist(x,bins=10,color='red',density=True)
   #density就是将数换成频率
   plt.show()   

   双变量直方图
     x=np.random.randn(1000)+2
     y=np.random.randn(1000)+3
     plt.hist2d(x,y,bins=40)
     plt.show()
     #颜色的深浅表示频率的大小

20.饼状图
   labels='a','b','c','d'
   fracs=[15,30,45,10]
   rc=[0,0,0.5,0]
   plt.pie(x=fracs,labels=labels,autopct='%.0f%%',explode=rc,shadow=True)
   plt.show()
   #显示百分比
   #突出显示c区
   #显示阴影

21.箱型图（box-plot）  
   又称为盒须图、盒式图或箱线图
   是一种用作显示一组数据分散情况资料的统计图
   上边缘，上四分位数，中位数，下四分位数，下边缘，异常值
   np.random.seed(100)
   data=np.random.normal(size=1000,loc=0,scale=1)
   plt.boxplot(data)
   plt.show()
  
22.三种方式
  22.1 pyplot：经典高层封装
  22.2 pylab：将matplotlib与numpy合并的模块，模拟matlab的编程环境
  22.3 面向对象的方式：matplotlab的精髓，更基础和底层的方式

23.爬虫的基本套路：
  23.1 基本流程
       ·目标数据
       ·来源地址
       ·结构分析
       ·实现构思
       ·操刀编码
  23.2 基本手段
         破解请求限制:
           ·请求头设置，如：uesragant为有校客户端
           ·控制请求频率（根据实际情景）
           ·ip代理
           ·签名/加密参数从html/cookie/js分析
         破解登录授权:
           ·请求带上用户cookie的信息
         破解验证码:
           ·简单的验证码可以使用识图验证码第三方库
  23.3 解析数据
         HTML dom解析:
           ·正则匹配，通过的正则表达式来匹配想要爬取的数据
             如有些数据不是在html标签里，而是在html的script标签的
             js变量中
           ·使用第三方库解析HTML dom，如类jquery的库
         数据字符串:
           ·正则匹配（根据情景使用）
           ·转json/xml对象进行解析

24.第一个
   from urllib.request import urlopen 
   response=urlopen("https://www.baidu.com/s?ie=utf-8&fr=bks0000&wd=JSON")
   print(response.read().decode())

   ctrl+f搜索

   from urllib.request import urlopen
   url = "https://www.baidu.com"
   # 发送请求
   response = urlopen(url)
   # 读取内容
   info = response.read()
   # 打印内容
   print(info.decode())

   ·request.urlopen(url,data,timeout)
      第一个参数为url，第二个参数data是访问url时要传送的数据，第三个timeout是设置超时时间
      第二三个参数是可以不传送的，data默认为 None ，timeout默认为socket._GLOBAL_DEFAULT_TIMEOUT
      第一个参数url是必须要传送的
   ·response.read()读取文件中的全部内容，返回bytes类型
   ·response.getcode()返回HTTP的响应码，成功返回200，4服务器页面出错，5服务器问题
   ·response.geturl()返回实际数据的实际url，防止重定向问题
   ·response.info()返回服务器相应的http报头

25.用requset对uesr-agant进行封装
   from urllib.request import urlopen
   from urllib.request import Request
   from random import choice

   user_agents = [
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE)",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
      "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
   ]

   url = "https://www.baidu.com/"
   headers = {
       "Uesr-Agent": choice(user_agents)
       # 随机选择一个user-agent
   }

   request = Request(url, headers=headers)
   response = urlopen(request)
   info = response.read()
   print(info.decode())

26.搜索转码
   ......
   from urllib.parse import quote
   # 导入转码包
   ......
   url = "https://www.baidu.com/s?wd={}".format(quote("闫文博"))
   # 在百度上中文搜索闫文博
   # 对“闫文博”中文进行转码
   ......
   省略号省略内容同上25

27.Get请求
   大部分被传到浏览器的html，image，js，css都是通过get方法发出请求的，它是获取数据的主要方法
   get请求的参数都是在url中体现的，如果有中文，需要转码，可以用
     ·urllib.parse.urlencode()
     ·urllib.prase.quote()

   第一个:
       from urllib.parse import urlencode
       headers=[就不写了参考上边]
       args={
               "wd":"闫文博"
               "ie":"utf-8"
               }
       url="网址/s?{}".format(urlencode(args))
       requset=Request(url,headers=headers)
       response=urlopen(request)
       info=response.read()
       print(info.decode())
       
   多参数时使用第一个方便一些

28.第一个实战例子：贴吧
   前排提醒：
   get_html中print要注释掉才会写入文件中

from urllib.request import urlopen
from urllib.request import Request
from random import choice
from urllib.parse import quote
from urllib.parse import urlencode
# 导入转码包

def get_html(url):
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    ]

    headers = {
        "Uesr-Agent": choice(user_agents)
        # 随机选择a一个user-agent
    }

    request = Request(url, headers=headers)
    response = urlopen(request)
    # print(response.read().decode())

    return response.read()

def save_html(filename, html_bytes):
    with open(filename, "wb") as f:
        f.write(html_bytes)
    # 开一个文件，第一个参数文件名,第二个参数格式
    # with open as 简化了文件流的读写，不需要try catch close

def main():
    content = input("请输入要下载的内容：")
    num = input("请输入要下载多少页：")
    base_url = "https://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):
        args = {
            "pn": pn * 50,
            "kw": content
        }
        args = urlencode(args)
        # print(base_url.format(args))
        html_bytes = get_html(base_url.format(args))
        # print(html_bytes)
        filename = "第" + str(pn) + "页.html"
        save_html(filename, html_bytes)
        print("正在下载" + filename)
        # 注意看缩进，在此条注释上面的依然在for循环中

if __name__ == '__main__':
    main()

29.post请求（必须字节）
   网页开发者工具勾选preserve log查看
   在Request Method中查看请求类型

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

url = "http://139.196.102.254/wp-login.php"
# 从from data中查看登录信息
from_data = {
    "log": "yqc",
    "pwd": "123456"
}
f_data = urlencode(from_data)
# 要先转码

# 依然是用header进行封装
headers = {
    "Uesr-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    # 随机选择一个user-agent
}

request = Request(url, data=f_data.encode(), headers=headers)
# 发送请求,记得转字节
response = urlopen(request)
print(response.read().decode())
# 获取请求并打印

30.ajax请求
   大概就跟豆瓣电影分类排行榜那种
   下拉式，滚动条快到底了再新加
   
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

base_url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=20"

# 依然是用header进行封装
headers = {
    "Uesr-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    # 选择一个user-agent
}

i = 0
while True:
    # 写一个死循环，当我不知道它总共有多少时用
    # 退出条件是返回的请求内容为空
    url = base_url.format(i * 20)
    request = Request(url, headers=headers)
    # 发送请求,记得转字节
    response = urlopen(request)
    info = response.read().decode()
    print(info)
    # 获取请求并打印
    if info =="" or info is None:
        break
    # 当不满足条件时退出循环
    i += 1
    # 否则的话让i+1继续
   
31. https请求 
    现在随处可见https开头的网站。urllib可以为https请求验证ssl证书
  就像web浏览器一样，如果网站的ssl证书是经过CA认证的，则能够正常访问
    如果ssl验证不通过，或者操作系统不信任服务器的安全证书，则需要：
      import ssl
      context = ssl.create_default_context()
      # 忽略验证证书
      response = urlopen(request, context=context)

32.proxy的使用
   透明代理：目标网站知道你使用了代理并且知道你的源ip地址
   匿名代理：匿名程度比较低，也就是网站知道你用代理，但是不知道你的源ip
   高匿代理：目标网站既不知道你使用的代理更不知道源ip
   from urllib.request import ProxyHandler
   from urllib.request import build_opener
   proxy = ProxyHandler({"这里写代理类型（http/https）": "[username]:[password]@这里写代理ip:端口号"})
   opener = build_opener(proxy)
   respoense = opener.open(url)
   print(respoense.read().decode("utf-8"))

33.cookie
   33.1 cookie,指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据
    比如说有些网站需要登录后才能访问某个页面，在登录之前，你想抓取某个页面的内容是不被允许的，
    那么我们可以利用urllib库保存我们登录的cookie
   
   33.2 opener
      当你获取一个url你使用一个opener(一个urllib.OpenerDirecor的实例)
    在前面，我们使用的都是一个默认的opener，也就是urlopen，它是一个
    特殊的opener，可以理解成opener的一个特殊实例，传入的参数仅仅是url、data、timeout

   33.3 cookielib
      cookielib模块的主要作用是提供可以存储的cookie对象,以便于urllib模块配合使用来访问internet资源
    ，cookielib模块非常强大，我们可以利用本模块的cookiejar类的对象来捕获cookie并在后续连接时重新发送
    比如可以实现模拟登录功能，该模块的主要对象有CookieJar\FileCookieJar\MozillaCookieJar\LWPCookieJar


   33.4 可以直接写入
      headers = {
          "Uesr-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
          # 选择一个user-agent
          "Cookie": "acw_tc=2760822416265728560473506e1a37c213ad7d4ac3b2093e82c8bcb6beb539; ASP.NET_SessionId=krr3gqim1awjb0t4d44uzyfu; _ga=GA1.2.498105644.1626572860; _gid=GA1.2.1759238132.1626572860; account=uB+SMSaQNdGCzA8Mh6PQA2GxNr9eppoRASFWqCwJN9QCW+/xzBXLr0JHhYylV/4GrzuMsVu+obSFrrEDaokizGGDvE6QqGJEIrP7JItGlf7/dm5K0o7etqWxCjfc/HyY; area=dbG"
      }

   33.5 也可以记录后再写
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.parse import urlencode
    from http import cookiejar
    # 转码
    from urllib.request import HTTPCookieProcessor, build_opener
    # 保存cookie信息

    login_url = "https://sso.sflep.com/cas/login?service=http%3a%2f%2fcourse.sflep.com%2f2019%2fuser%2floginredirect.aspx"
    # 依然是用header进行封装
    headers = {
    "Uesr-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    # 选择一个user-agent
    }
    from_data = {
    "username": "15324730588",
    "password": "WOyaokaoyan7!",
    "submit": "登录"
    }
    # 设置登录账号密码
    f_data = urlencode(from_data).encode()
    # 转码
    request = Request(login_url, headers=headers, data=f_data)
    # response = urlopen(request)
    # 然后就不用它了↑
    handler = HTTPCookieProcessor()
    cookie = cookiejar.CookieJar()
    opener = build_opener(handler)
    response = opener.open(request)
    # 发送请求并接受响应
    # print(response.read().decode())
    for item in cookie:
    print('Name = %s' % item.name)
    print('Value = %s' % item.value)
    # 打印coolie信息

    # 访问页面
    url = "https://course.sflep.com/2019/Student/course_info.aspx?cid=64"
    request = Request(url, headers=headers)
    # response = urlopen(request)
    response = opener.open(request)
    info = response.read().decode()
    print(info)


   33.6 先保存到文件后读取文件 
    from urllib.request import Request
    from urllib.parse import urlencode
    from http import cookiejar
    # 转码
    from urllib.request import HTTPCookieProcessor, build_opener
    # 保存cookie信息

    def get_cookie():
        login_url = "http://139.196.102.254/wp-login.php"
        # 依然是用header进行封装
        headers = {
            "Uesr-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            # 选择一个user-agent
        }
        from_data = {
            "log": "yqc",
            "pwd": "123456",
            "wp-submit": "登录"
        }
        # 设置登录账号密码
        f_data = urlencode(from_data).encode()
        # 转码
        request = Request(login_url, headers=headers, data=f_data)
        cookie = cookiejar.MozillaCookieJar()
        handler = HTTPCookieProcessor(cookie)
        opener = build_opener(handler)
        response = opener.open(request)
        # print(response.read().decode())
        cookie.save("111.txt", ignore_expires=True, ignore_discard=True)
        use_cookie()

    def use_cookie():
        info_url = "http://139.196.102.254/wp-admin/profile.php"
        headers = {
            "Uesr-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            # 选择一个user-agent
        }
        request = Request(info_url, headers=headers)
        cookie = cookiejar.MozillaCookieJar()
        cookie.load("111.txt", ignore_discard=True, ignore_expires=True)
        handler = HTTPCookieProcessor(cookie)
        opener = build_opener(handler)
        response = opener.open(request)
        print(response.read().decode())

    if __name__ == '__main__':
        get_cookie()   

36.requests库的基本使用
   import requests

   36.1 基本请求
     ·req=requests.get("网址")
     ·req=requests.post("网址")
     ·req=requests.put("网址")
     ·req=requests.delete("网址")
     ·req=requests.head("网址")
     ·req=requests.options("网址")
     
   36.2 get请求


