 
                              python����ѧ��ģ


1.�������ͣ�������������������ֵ����ֵ
2.�ַ����������������壬������˫�����ǵȼ۵�
  a='hello world' ��a="hellw world"
  
  2.1��������������������������ֵ��ַ���
      s='''hello
        my
        world'''

  2.2���ַ����ӷ�
      s="hello"+"world"

  2.3���ַ���������
      ��������c++��ͬ�Ǵ�0��ʼ��
      s[������]
      s[0]

  2.4���ַ����ķָ�
      s="hello world"
      Ĭ���ǰ��տո����ָ��
      s.split()
      ['hello','world']

      2.4.1)�Զ���ָ�����
          s.split(',')

  2.5���鿴�ַ�������
      len(�ַ���)
      len(s)

3.��������
  3.1��**�����㣬����x��y����
  3.2��//ȡ���� �����̵��������֣�����ȡ����

4.�߼�����
  4.1��and ��x and y ����"��"�����xΪfalse����x and y ����false�����򷵻�y��ֵ
  4.2��or��x or y ����"��"�����xΪ��0��������x��ֵ�����򷵻�y��ֵ
  4.3��not x������"��"�����xΪtrue������false�����xΪfalse��������true


5.���ݽṹ
  5.1���б�List����[]���ɣ�Ҳ������list
       ��list('abcde')

       5.1.1)�б����
             a=[1,2,3,4,5]
             actor=['s', 'd', 'n', 'f']
             a+actor
             Out[20]: [1, 2, 3, 4, 5, 's', 'd', 'n', 'f']

       5.1.2)�б�ȡֵ
             a[������]#���㿪ʼ
             ��a[0]=1

       5.1.3)�б�׷��
             a.append(6)
             out:[1,2,3,4,5,6]

       5.1.4)�б����
             a.insert(������,ֵ)
             a.insert(1,10)
             out:[1,10,2,3,4,5,6]

       5.1.5)Ԫ��ɾ��
             a.pop()#ɾ����ĩβ��
             a.pop(1)#ɾ��������Ϊ1������Ԫ��
                     #���������ɴ�0��ʼ
                     
       5.1.6����Ƭ
             ��ʱa=[1,2,3,4,5]
             1.6.1��a[0:3]#����ҿ����䣬����a����ȡ��1��2��3

             1.6.2��Ҳ����a[:3]#Ĭ�ϴ���ߵ�һ��Ԫ�ؿ�ʼ��ȡ�����ͬ��

             1.6.3��a[0:]#ð���ұ߲�д��Ĭ��ȡ�����һ��Ԫ��
                         #��a����ȡ������
                      
             1.6.4��a[0:-1]#ȡ���������һλ��ǰһλ
                           #�����[1,2,3,4]
                           
             1.6.5)b=[1,2,3,4,5,6,7,8,9,10]
                   b[a:b:i]#��aȡ��b�����ǲ�����b���Լ��iΪ��������ȡֵ
                   b=[1,2,3,4,5,6,7,8,9,10]
                   b[2:9:3]
                   Out[2]: [3, 6, 9]#д�����Ӻ���ǰȡֵ

            
  5.2��Ԫ��tuple����()��ʾ����list���ƣ�����tupleһ������ʼ���Ͳ����޸�

  5.3���ֵ�dict����{key:value}����dictionary���������ݿ������κ����ͣ������ֵ�
             mv={'name':'Ф��˵ľ���', 'actor':'�ޱ�˹', 'score':9.6 ,'country':'USA'}
             3.1����ѯ
                  mv['name']
                  out:'Ф��˵ľ���'
             3.2������ѯ
                  mv.keys()
                  out:dict_keys(['name', 'actor', 'score'])
             3.4��ֵ��ѯ
                  mv.value()
                  out:dict_values(['Ф��˵ľ���', 'robins', 9.6])
             3.5��ȫ����ѯ
                  mv.items()
                  dict_items([('name', 'Ф��˵ľ���'), ('actor', 'robins'), ('score', 9.6)])

             3.6���޸�
                  mv['name']='̩̹��˺�'
              
             3.7�����
                  mv['director']='��������'

             3.8��ɾ��
                  mv.pop('director')#�����Ǽ�


  5.4������set����{}�����ɼ��ϣ������в�������ͬԪ��
       #�����в��ܺ����κ���ͬԪ�أ�������{}��ʾ
       ������ len() ���в鿴
       ����� add()

       4.1������
               s={2,3,4,5}
               s1={1,2,3,4}
               s&s1
       Out[11]: {2, 3, 4}

       4.2������
               s|s1
       Out[12]: {1, 2, 3, 4, 5}

       4.3������
            s-s1 #����s���ǲ�����s1��һЩԪ��


6.�ɱ�����벻�ɱ����
     
  6.1���ɱ������Զ�����в��롢ɾ���Ȳ��������ɱ���󲻿��Զ�������иı�Ĳ���
       python���б��ֵ䣬���ϵȶ��ǿɱ�ģ�Ԫ�飬�ַ��������͵ȶ��ǲ��ɱ�� 


7.����ת��
  int(3.14)
  3
  float(3)
  3.0

  �鿴��������
  s='adffsa'
  type(s)
  str

8.�жϺ�ѭ��  

  8.1��2==2     True
       3=='a'   False
       'a'=='A' False 
       #python�����ִ�Сд

  8.2��if 2>1:
           print('hellow')

       �ж����

  8.3��a=1
       b=2
       if a>b:
           print('a>b')
       else:    
           print('a<=b')
    
       out:a<=b
  
  8.4��x=0
       if x>0:
           print('x>0')
       elif x==0:
           print('x=0')
       else:
           print('x<0')

  8.5��ѭ��
      8.5.1��for ѭ��
             for i in [1,2,3,4,5,6,7,8,9]
                 print(i)
             �ڷ�Χ�ڽ���ѭ��
      
      8.5.2��while ѭ��
             while i<10:
                 print(i)
                 i=i+1

  8.6���б�����ʽ
       ��List Comprehensions����python���õķǳ���ȴǿ��Ŀ�����������list������ʽ
       list(range(1,11))  #range(1,11)����ҿ�����
       out:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

       [x**2 for x in range(1,10)]
       out:[1, 4, 9, 16, 25, 36, 49, 64, 81]
       
       ���������ж�
       [i for i in range(1,100) if i%10==0]
       out:[10, 20, 30, 40, 50, 60, 70, 80, 90]
       
       ת��
       [str(x) for x in range(1,10)]
       ['1', '2', '3', '4', '5', '6', '7', '8', '9']

       ת������
       [int(x) for x in list('123456789')]
       [1, 2, 3, 4, 5, 6, 7, 8, 9]


9.����
  9.1���������ú���  
       abs(-1) #ȡ����ֵ

       a=[1,3,-9,10,34]
       max(a)  #�����ֵ
       min(a)  #����Сֵ
       sum(a)  #���

  9.2���Զ��庯��
       ����function��ͨ������������������з���ֵ
       ������
          ʹ�� def �ؼ���������һ������
          def ������Ǻ��������ƣ��������Ǻ����Ĳ�������ͬ�Ĳ�����.����
          def func()����ʽ����Ҫ�У���������Ϊ��
          ʹ�����������ֺ���������
          return �����ض���ֵ�����ʡ�ԣ����� None

       def add(x,y):
           a=x+y
           return a
       print(add(2,3))
       
       ���Ը�����Ĭ��ֵ

10.�������
    10.1 import numpy
    10.2 import numpy as np
    10.3 from numpy import *  #���Բ���дǰ׺.���ǲ�����ȥд

11.numpy�������ϵĲ���
    11.1���б���ÿ��Ԫ������1
        11.1.1ʹ���б�����ʽ��
                a=[1,2,3,4]
                [x+1 for x in a]
              ����ʹ��a+1

        11.1.2 ʹ��numpy
                a=np.array([1,2,3,4])
                a+1
                a*2

    11.2�б����   
        11.2.1 b=[2,3,4,5]
              ��ʱ��a+bʵ�ֵ����б��ƴ��
              ʹ���б�����ʽ��
                 [x+y for (x,y) in zip(a,b)]
        
        11.2.2ʹ��numpy
                b=np.array([2,3,4,5])
                a+b

    11.3��������
        11.3.1���б�������飺
          l=[0,1,2,3]
          a=np.array(l)

        11.3.2���б��룺
          a=np.array([1,2,3,4])

        11.3.3����ȫ��0�����飺
          a=np.zeros(5)

        11.3.4����ȫ��1�����飺
          a=np.noes(5,dtype='int')
          #dtypeд��������
        
        11.3.5��fill������������Ϊָ��ֵ��
          a.fill(5)
          #fillҪ���б���ÿ��Ԫ�ص�����������һ�µ�
          ��a�����������͵ĸ���
          a=a.astype('float')

        11.3.6������������
          a=np.arange(1,10)
          #����ҿ�����
          ������������д�ɲ���

        11.3.7���ɵȲ����У� 
          a=np.linspace(1,10,21)
          ��1��10һ��21�����ĵȲ�����
          #������ҿ�����

        11.3.8���������  
          a=np.random.rand(10)
          #����0~1֮���ʮ����ͬ�����������
          a=np.random.randn(10)
          #���ط�����̬�ֲ��������
          a=np.random.randint(1,10,10)
          #����1-10֮��ʮ���������
          
    11.4��������
        11.4.1�鿴���ͣ�
            type(a)
        11.4.2�鿴�����ڲ��������ͣ�
            a.dtype
        11.4.3�鿴��״���᷵��һ��Ԫ�飬ÿ��Ԫ�ش�����һά��Ԫ����Ŀ
            a.shape
            np.shape(a)
        11.4.5�鿴��������Ԫ�ص���Ŀ��
            a.size
        11.4.6�鿴�����ά�ȣ�
            a.ndim

    11.5��������Ƭ
        11.5.1������һ��Ԫ�أ�
            a=np.array([0,1,2,3])
            #�����Ŵ�0��ʼ
            a[0]       0
            �޸�
            a[0]=10

        11.5.2��Ƭ(֧�ָ�����)
            a=np.array([11,12,13,141,15])
            a[1:3]#����ҿ���0��ʼ
            a[1:-2]#��������Ϊ1������ʼȡ��ȡ�������ڶ���Ԫ�ص�ǰһ��Ԫ��
            a[-4:3]#�ӵ������ĸ�Ԫ�ؿ�ʼȡ��ȡ����������
            ��������ֵ��ͬ
            
12.��ά����
    12.1 ��ά���������
         a=np.array([[0,1,2,3],[10,11,12,13]])
         ʵ���ϴ������һ�����б�ΪԪ�ص��б�
         ���鿴��״
           a.shape
           (2,4)#��������
         ���鿴Ԫ�ظ���
           a.size
         ���鿴ά��
           a.ndim

    12.2��ά���������
         ���ڶ�ά���飬���Դ�����������������
         ���ϵ�a[1,3]
         1����������3�����������м��ö��Ÿ�������0��ʼ
         ���������������и�ֵ
         a[1,3]=-1
         
    12.3��ά����ĵ�������
         a[1]���������ŵĵ�һ�е�����

    12.4��ά�������Ƭ
        a=np.array([[0,1,2,3,4,5],
                    [10,11,12,14,13,15],
                    [20,21,22,23,24,25],
                    [30,31,32,33,34,35],
                    [40,41,42,43,44,45],
                    [50,51,52,53,54,55]])
        ���õ���һ�еĵ��ĸ��͵����Ԫ��
           a[0,3:5]
        ���õ�������е��������(44,45,54,55) 
           a[4:,4:]
        ���õ�������(2,12,22,32,42,52)
           a[:,2]

        ÿһά��֧����Ƭ�Ĺ��򣬰�����������ʡ��:
            [lower:upper:step]
  
        ȡ��3��5�е������У�
           a[2::2,::2]

    12.5��ʽ����
        ��Ƭֻ֧���������ߵȼ������Ƭ������Ҫʵ������λ�õĲ���
      ��Ҫʹ�û�ʽ����fancy slicing
        
        12.5.1һά��ʽ����
          ��range�������ƣ����ǿ���ʹ��arange�����������Ȳ�����
          a=np.arange(0,100,10)
          
          ��ʽ������Ҫָ������λ��:
              index=[1,2,-3]
              y=a[index]
              print(y)
          ȡ��ֵ�ǵ�1��2��-3λ���ϵ�ֵ

          ����ʹ�ò�����������ʽ����
           mask=np.array([0,2,2,0,0,1,0,0,1,0],dtype=bool)
          mask�����ǲ������顣���ȱ�������鳤����� 
           a[mask]
          ȡ������λ��Ϊtrue(��0)����
        
        12.5.2��ά��ʽ����(��12.4������)
          ������һ���ζԽ����ϵ�5��ֵ(1,12,23,34,45)
            ��д��ֵ����д��ֵ
            a[(0,1,2,3,4),(1,2,3,4,5)]

          ������������е�1��3��5��
            a[3:,[0,2,4]]
          ����Ƭ��ͬ����ʽ�������ص���ԭ�����һ�����ƶ���������

     12.6����ȫ����
        ��ֻ������������ʱ�򣬷������У�
          y=a[:3]#���ص���ǰ����
        ��Ҳ�����û�ʽ����������2��3��5��:
            con=np.array([0,1,1,0,1,0],dtype=bool)
            a[con]

13. where��� 
   where(array)
   where�����᷵�����з���Ԫ�ص�����
   
   a=np.array([0,12,5,20])
   �ж������е�Ԫ���ǲ��Ǵ���10��
     a>10
     array([False,True,False,True],dtype=bool)
   
   ���������д���10��Ԫ�ص�����λ��:
     np.where(a>10)
     (array([1,3],dtype=int64),)

   ע�⣬where�ķ���ֵ��һ��Ԫ�飬���ص�������λ�ã�����[1,3]����10����
   Ҳ����ֱ�����������
     a[a>10]
     array([12,20])
     a[np.where(a>10)]

14.����ת��
   ������a=np.array([1.5,-3],dtype=float)
   Ҳ������asarray
     14.1 np.asarray(a,dtype=float)

     14.2 astype����
       a=np.array([1,2,3])
       a.astype(float)
       û�и�ֵ��a��ʵ����a��ֵ��û�з����ı�

15.�������
   ���ݣ�
   import numpy as np
   mv_name=['Ф��˵ľ���','�ط�֤��','��������','��������','������','̩̹��˺�','�����յ�����','���ɱ�ֲ�̫��','����','����']
   mv_num=np.array([692795,42995,327855,580987,478523,127074,306904,662552,284652,159302])
   mv_score=np.array([9.6,9.5,9.5,9.4,9.4,9.4,9.4,9.3,9.3,9.3])
   mv_length=np.array([142,116,116,142,171,194,195,133,109,92])
   #��Ӱ�����������������֡���Ӱʱ��

   15.1 ��������
     15.1.1 sort����
       np.sort(mv_num)
       ��Ȼû�иĶ�ԭ����
     
     15.1.2 argsort����
       ���ش�С����������������е�����λ��
       �鿴�������ٵĵ�Ӱ����
       order=np.argsort(mv_num)
       mv_name[order[0]]#ע�⣬����д��������λ��

   15.2 ���:np.sum(mv_num)����mv_num.sum()
        ���ֵ:np.max(mv_length)����mv_length.max()
        ��Сֵ:min,
        ��ֵ:mean
        ��׼��:std
        ���ϵ������:cov(mv_score,mv_length)
        
   15.3 ��ά����Ĳ���
      15.3.1 ������״
        reshape�������޸�ԭ�������ֵ�����Ƿ���һ��������
        a=np.arange(6)
        a.shape=2,3#ת���������еĶ�ά���� �޸���a��ֵ

      15.3.2 ת�ã�
        a=a.reshape(2,3)
        a.T����a.transpose()
        ע�⣺û�и�ֵ��a������ôa���鱾���ǲ���仯��

   15.4 �������ӣ�concatenate
        concatenate((a0,a1,...,an),axis=0)
        Ĭ���ǰ�����������ƴ��
        ����ǰ���������ƴ�ӣ���ô��Ҫ��axis�ĳ�1
        ��Щ����Ҫ��()������һ��Ԫ����ȥ
        ���˸������⣬�����᳤�ȱ�����һ����

        ���ݵ�һά�������ӣ�
          x=np.array([[0,1,2],[10,11,12]])
          y=np.array([[50,51,52],[60,61,62]])
          z=np.concatenate((x,y))
          z=array([[ 0,  1,  2],
                   [10, 11, 12],
                   [50, 51, 52],
                   [60, 61, 62]])
          ��Ӧ�Ŀ���ʹ��np.vstack((x,y))#�ѵ�

        ���ݵڶ�ά����ƴ�ӣ�
          z=np.concatenate((x,y),axis=1)
          z=array([[ 0,  1,  2, 50, 51, 52],
                   [10, 11, 12, 60, 61, 62]])
          ��Ӧ�Ŀ���ʹ��np.hstack((x,y))

        ��Ϊx,y��״��һ���ģ������Խ�����ƴ�ӳ���ά�����飬ֻ��concatenate���ṩ
          z=np.array((x,y))
          z=array([[[ 0,  1,  2],
                    [10, 11, 12]],
                    
                   [[50, 51, 52],
                    [60, 61, 62]]])
        
        ά�ȵĻ�������np.dstack((x,y))

        ����ֵ��abs
        ָ����exp
        ��ֵ��media
        �ۼƺͣ�cumsum


16.ɢ��ͼ
   import numpy as np
   import matplotlib.pyplot as plt
   height=[123,214,352,123,234,1231,3]
   weight=[121,432,23,123,43,123,565]
   plt.scatter(height,weight)
   plt.show()
   
   ��ȡscv���ݲ������л���ɢ��ͼ
     import pandas as pd
     iris = pd.read_csv("demand_2016.03.10_510100_.csv")
      #ע�⣺���·������ӵ���ĿĿ¼�µ��ļ�·��
     plt.scatter(iris.loc[1:,'longitude'],iris.loc[1:,'latitude'])
     plt.show()
      #ѡȡ�ӵ�2�е����һ�У�longitude��latitude�н��л���

     ѡȡ��11��12��ʱ�̵�����
     iris[(iris['hour']==12)|(iris['hour']==11)] 

   ��۵�����
     �����С��s
        plt.scatter(iris.loc[1:,'longitude'],iris.loc[1:,'latitude'],s=10)
       s���������ֱ��
     ����ɫ��c
        c='r'#����ɫ��Ϊ��ɫ��Ĭ������ɫ�ģ�Ҳ����b
     ����״��marker  
     ��͸���ȣ�alpha

   ������ʾx���꣬y���꣬ͼ��
     #-*- coding: utf-8 -*
     import matplotlib as mt
     font ={'family':'MicroSoft YaHei'} #win������ʾ����
     mt.rc("font",**font)
     plt.scatter(iris.loc[1,'����������'],iris.loc[1,'������γ��'],c='r')
     plt.scatter(iris.loc[2:,'����������'],iris.loc[2:,'������γ��'],c='b')
     plt.xlabel('����������')
     plt.ylabel('������γ��')
     plt.title('�������ֲ�ʾ��ͼ')
     plt.show()


17.����ͼ
   linespace(-10,10,100)
   #���ɵ������һ����
   #�����Ǵ�-10��ʼ��10��ƽ���ֳ�100��
   x=np.linspace(-10,10,100)
   y=x**3
   plt.plot(x,y)
   plt.show()

   ���ƴ���ʱ�������ͼ
     import matplotlib.dates as mdates
     date,open,close=np.load('00001.scv',delimiter=','
             converters={0:mdates.strpdate2num('%m/%d/%y')},
             #1/1/2001 ��������ʱ������/��/��ĸ�ʽ����
             skiprows=1,usecols=(0,1,4),#����0��1��4��
             unpack=True)
     plt.plot_date(date,open,'-')
     #-�����߶�
    
   ����˵��
     ��linestyle:����
     ��color����ɫ
     ��marker����״
     plt.xticks����x��Ŀ̶�

18.����ͼ
   ��ֱ��������ͼ
     n=5
     y=[20,10,30,25,15]
     index=[10,15,20,15,30]
     a=[1,2,3,4,5]
     pl=plt.bar(x=index,height=y,width=0.1)
     plt.show()

   ����������ͼ
     n=5
     index=[10,15,20,15,30]
     a=[1,2,3,4,5]
     pl=plt.barh(y=index,height=2,width=a)
     plt.show()

   ˫�д�ֱ����ͼ
     index=np.arange(4)
     sales_bj=[52,55,63,53]
     sales_sh=[44,66,55,41]
     bar_width=0.3
     plt.bar(index,sales_bj,bar_width,color='b',label="the first bar")
     plt.bar(index+bar_width,sales_sh,bar_width,color='r',label="the second bar")
     plt.legend(loc='upper left')
     plt.show()
     #������ʾֱ�ߺ���
   
   ���д�ֱ��������ͼ
     index=np.arange(4)
     sales_bj=[52,55,63,53]
     sales_sh=[44,66,55,41]
     bar_width=0.3
     plt.bar(index,sales_bj,bar_width,color='b',label="the first bar")
     plt.bar(index,sales_sh,bar_width,color='r',label='the second bar',bottom=sales_bj)
     plt.legend(loc='upper left')
     plt.show()

   ����˵��
     ��color����ɫ
     ��alpha��͸����
     ��edgecolor��ͼ�α�Ե��ɫ
     ��legend��loc��������:
         'best'         : 0, (only implemented for axes legends)(����Ӧ��ʽ)
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
     ��linewidth or linewidths or lw����Եor�ߵĿ�    

19.ֱ��ͼ
   mu=100
   sigma=20
   x=mu+sigma*np.random.randn(2000)
   plt.hist(x,bins=10,color='red',density=True)
   #density���ǽ�������Ƶ��
   plt.show()   

   ˫����ֱ��ͼ
     x=np.random.randn(1000)+2
     y=np.random.randn(1000)+3
     plt.hist2d(x,y,bins=40)
     plt.show()
     #��ɫ����ǳ��ʾƵ�ʵĴ�С

20.��״ͼ
   labels='a','b','c','d'
   fracs=[15,30,45,10]
   rc=[0,0,0.5,0]
   plt.pie(x=fracs,labels=labels,autopct='%.0f%%',explode=rc,shadow=True)
   plt.show()
   #��ʾ�ٷֱ�
   #ͻ����ʾc��
   #��ʾ��Ӱ

21.����ͼ��box-plot��  
   �ֳ�Ϊ����ͼ����ʽͼ������ͼ
   ��һ��������ʾһ�����ݷ�ɢ������ϵ�ͳ��ͼ
   �ϱ�Ե�����ķ�λ������λ�������ķ�λ�����±�Ե���쳣ֵ
   np.random.seed(100)
   data=np.random.normal(size=1000,loc=0,scale=1)
   plt.boxplot(data)
   plt.show()
  
22.���ַ�ʽ
  22.1 pyplot������߲��װ
  22.2 pylab����matplotlib��numpy�ϲ���ģ�飬ģ��matlab�ı�̻���
  22.3 �������ķ�ʽ��matplotlab�ľ��裬�������͵ײ�ķ�ʽ

23.����Ļ�����·��
  23.1 ��������
       ��Ŀ������
       ����Դ��ַ
       ���ṹ����
       ��ʵ�ֹ�˼
       ���ٵ�����
  23.2 �����ֶ�
         �ƽ���������:
           ������ͷ���ã��磺uesragantΪ��У�ͻ���
           ����������Ƶ�ʣ�����ʵ���龰��
           ��ip����
           ��ǩ��/���ܲ�����html/cookie/js����
         �ƽ��¼��Ȩ:
           ����������û�cookie����Ϣ
         �ƽ���֤��:
           ���򵥵���֤�����ʹ��ʶͼ��֤���������
  23.3 ��������
         HTML dom����:
           ������ƥ�䣬ͨ����������ʽ��ƥ����Ҫ��ȡ������
             ����Щ���ݲ�����html��ǩ�������html��script��ǩ��
             js������
           ��ʹ�õ����������HTML dom������jquery�Ŀ�
         �����ַ���:
           ������ƥ�䣨�����龰ʹ�ã�
           ��תjson/xml������н���

24.��һ��
   from urllib.request import urlopen 
   response=urlopen("https://www.baidu.com/s?ie=utf-8&fr=bks0000&wd=JSON")
   print(response.read().decode())

   ctrl+f����

   from urllib.request import urlopen
   url = "https://www.baidu.com"
   # ��������
   response = urlopen(url)
   # ��ȡ����
   info = response.read()
   # ��ӡ����
   print(info.decode())

   ��request.urlopen(url,data,timeout)
      ��һ������Ϊurl���ڶ�������data�Ƿ���urlʱҪ���͵����ݣ�������timeout�����ó�ʱʱ��
      �ڶ����������ǿ��Բ����͵ģ�dataĬ��Ϊ None ��timeoutĬ��Ϊsocket._GLOBAL_DEFAULT_TIMEOUT
      ��һ������url�Ǳ���Ҫ���͵�
   ��response.read()��ȡ�ļ��е�ȫ�����ݣ�����bytes����
   ��response.getcode()����HTTP����Ӧ�룬�ɹ�����200��4������ҳ�����5����������
   ��response.geturl()����ʵ�����ݵ�ʵ��url����ֹ�ض�������
   ��response.info()���ط�������Ӧ��http��ͷ

25.��requset��uesr-agant���з�װ
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
       # ���ѡ��һ��user-agent
   }

   request = Request(url, headers=headers)
   response = urlopen(request)
   info = response.read()
   print(info.decode())

26.����ת��
   ......
   from urllib.parse import quote
   # ����ת���
   ......
   url = "https://www.baidu.com/s?wd={}".format(quote("���Ĳ�"))
   # �ڰٶ��������������Ĳ�
   # �ԡ����Ĳ������Ľ���ת��
   ......
   ʡ�Ժ�ʡ������ͬ��25

27.Get����
   �󲿷ֱ������������html��image��js��css����ͨ��get������������ģ����ǻ�ȡ���ݵ���Ҫ����
   get����Ĳ���������url�����ֵģ���������ģ���Ҫת�룬������
     ��urllib.parse.urlencode()
     ��urllib.prase.quote()

   ��һ��:
       from urllib.parse import urlencode
       headers=[�Ͳ�д�˲ο��ϱ�]
       args={
               "wd":"���Ĳ�"
               "ie":"utf-8"
               }
       url="��ַ/s?{}".format(urlencode(args))
       requset=Request(url,headers=headers)
       response=urlopen(request)
       info=response.read()
       print(info.decode())
       
   �����ʱʹ�õ�һ������һЩ

28.��һ��ʵս���ӣ�����
   ǰ�����ѣ�
   get_html��printҪע�͵��Ż�д���ļ���

from urllib.request import urlopen
from urllib.request import Request
from random import choice
from urllib.parse import quote
from urllib.parse import urlencode
# ����ת���

def get_html(url):
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; InfoPath.2; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; 360SE)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    ]

    headers = {
        "Uesr-Agent": choice(user_agents)
        # ���ѡ��aһ��user-agent
    }

    request = Request(url, headers=headers)
    response = urlopen(request)
    # print(response.read().decode())

    return response.read()

def save_html(filename, html_bytes):
    with open(filename, "wb") as f:
        f.write(html_bytes)
    # ��һ���ļ�����һ�������ļ���,�ڶ���������ʽ
    # with open as �����ļ����Ķ�д������Ҫtry catch close

def main():
    content = input("������Ҫ���ص����ݣ�")
    num = input("������Ҫ���ض���ҳ��")
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
        filename = "��" + str(pn) + "ҳ.html"
        save_html(filename, html_bytes)
        print("��������" + filename)
        # ע�⿴�������ڴ���ע���������Ȼ��forѭ����

if __name__ == '__main__':
    main()

29.post���󣨱����ֽڣ�
   ��ҳ�����߹��߹�ѡpreserve log�鿴
   ��Request Method�в鿴��������

from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

url = "http://139.196.102.254/wp-login.php"
# ��from data�в鿴��¼��Ϣ
from_data = {
    "log": "yqc",
    "pwd": "123456"
}
f_data = urlencode(from_data)
# Ҫ��ת��

# ��Ȼ����header���з�װ
headers = {
    "Uesr-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    # ���ѡ��һ��user-agent
}

request = Request(url, data=f_data.encode(), headers=headers)
# ��������,�ǵ�ת�ֽ�
response = urlopen(request)
print(response.read().decode())
# ��ȡ���󲢴�ӡ

30.ajax����
   ��ž͸������Ӱ�������а�����
   ����ʽ���������쵽�������¼�
   
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

base_url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=20"

# ��Ȼ����header���з�װ
headers = {
    "Uesr-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    # ѡ��һ��user-agent
}

i = 0
while True:
    # дһ����ѭ�������Ҳ�֪�����ܹ��ж���ʱ��
    # �˳������Ƿ��ص���������Ϊ��
    url = base_url.format(i * 20)
    request = Request(url, headers=headers)
    # ��������,�ǵ�ת�ֽ�
    response = urlopen(request)
    info = response.read().decode()
    print(info)
    # ��ȡ���󲢴�ӡ
    if info =="" or info is None:
        break
    # ������������ʱ�˳�ѭ��
    i += 1
    # ����Ļ���i+1����
   
31. https���� 
    �����洦�ɼ�https��ͷ����վ��urllib����Ϊhttps������֤ssl֤��
  ����web�����һ���������վ��ssl֤���Ǿ���CA��֤�ģ����ܹ���������
    ���ssl��֤��ͨ�������߲���ϵͳ�����η������İ�ȫ֤�飬����Ҫ��
      import ssl
      context = ssl.create_default_context()
      # ������֤֤��
      response = urlopen(request, context=context)

32.proxy��ʹ��
   ͸������Ŀ����վ֪����ʹ���˴�����֪�����Դip��ַ
   �������������̶ȱȽϵͣ�Ҳ������վ֪�����ô������ǲ�֪�����Դip
   �������Ŀ����վ�Ȳ�֪����ʹ�õĴ������֪��Դip
   from urllib.request import ProxyHandler
   from urllib.request import build_opener
   proxy = ProxyHandler({"����д�������ͣ�http/https��": "[username]:[password]@����д����ip:�˿ں�"})
   opener = build_opener(proxy)
   respoense = opener.open(url)
   print(respoense.read().decode("utf-8"))

33.cookie
   33.1 cookie,ָĳЩ��վΪ�˱���û���ݡ�����session���ٶ��������û������ն��ϵ�����
    ����˵��Щ��վ��Ҫ��¼����ܷ���ĳ��ҳ�棬�ڵ�¼֮ǰ������ץȡĳ��ҳ��������ǲ�������ģ�
    ��ô���ǿ�������urllib�Ᵽ�����ǵ�¼��cookie
   
   33.2 opener
      �����ȡһ��url��ʹ��һ��opener(һ��urllib.OpenerDirecor��ʵ��)
    ��ǰ�棬����ʹ�õĶ���һ��Ĭ�ϵ�opener��Ҳ����urlopen������һ��
    �����opener����������opener��һ������ʵ��������Ĳ���������url��data��timeout

   33.3 cookielib
      cookielibģ�����Ҫ�������ṩ���Դ洢��cookie����,�Ա���urllibģ�����ʹ��������internet��Դ
    ��cookielibģ��ǳ�ǿ�����ǿ������ñ�ģ���cookiejar��Ķ���������cookie���ں�������ʱ���·���
    �������ʵ��ģ���¼���ܣ���ģ�����Ҫ������CookieJar\FileCookieJar\MozillaCookieJar\LWPCookieJar


   33.4 ����ֱ��д��
      headers = {
          "Uesr-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
          # ѡ��һ��user-agent
          "Cookie": "acw_tc=2760822416265728560473506e1a37c213ad7d4ac3b2093e82c8bcb6beb539; ASP.NET_SessionId=krr3gqim1awjb0t4d44uzyfu; _ga=GA1.2.498105644.1626572860; _gid=GA1.2.1759238132.1626572860; account=uB+SMSaQNdGCzA8Mh6PQA2GxNr9eppoRASFWqCwJN9QCW+/xzBXLr0JHhYylV/4GrzuMsVu+obSFrrEDaokizGGDvE6QqGJEIrP7JItGlf7/dm5K0o7etqWxCjfc/HyY; area=dbG"
      }

   33.5 Ҳ���Լ�¼����д
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.parse import urlencode
    from http import cookiejar
    # ת��
    from urllib.request import HTTPCookieProcessor, build_opener
    # ����cookie��Ϣ

    login_url = "https://sso.sflep.com/cas/login?service=http%3a%2f%2fcourse.sflep.com%2f2019%2fuser%2floginredirect.aspx"
    # ��Ȼ����header���з�װ
    headers = {
    "Uesr-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    # ѡ��һ��user-agent
    }
    from_data = {
    "username": "15324730588",
    "password": "WOyaokaoyan7!",
    "submit": "��¼"
    }
    # ���õ�¼�˺�����
    f_data = urlencode(from_data).encode()
    # ת��
    request = Request(login_url, headers=headers, data=f_data)
    # response = urlopen(request)
    # Ȼ��Ͳ������ˡ�
    handler = HTTPCookieProcessor()
    cookie = cookiejar.CookieJar()
    opener = build_opener(handler)
    response = opener.open(request)
    # �������󲢽�����Ӧ
    # print(response.read().decode())
    for item in cookie:
    print('Name = %s' % item.name)
    print('Value = %s' % item.value)
    # ��ӡcoolie��Ϣ

    # ����ҳ��
    url = "https://course.sflep.com/2019/Student/course_info.aspx?cid=64"
    request = Request(url, headers=headers)
    # response = urlopen(request)
    response = opener.open(request)
    info = response.read().decode()
    print(info)


   33.6 �ȱ��浽�ļ����ȡ�ļ� 
    from urllib.request import Request
    from urllib.parse import urlencode
    from http import cookiejar
    # ת��
    from urllib.request import HTTPCookieProcessor, build_opener
    # ����cookie��Ϣ

    def get_cookie():
        login_url = "http://139.196.102.254/wp-login.php"
        # ��Ȼ����header���з�װ
        headers = {
            "Uesr-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
            # ѡ��һ��user-agent
        }
        from_data = {
            "log": "yqc",
            "pwd": "123456",
            "wp-submit": "��¼"
        }
        # ���õ�¼�˺�����
        f_data = urlencode(from_data).encode()
        # ת��
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
            # ѡ��һ��user-agent
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

36.requests��Ļ���ʹ��
   import requests

   36.1 ��������
     ��req=requests.get("��ַ")
     ��req=requests.post("��ַ")
     ��req=requests.put("��ַ")
     ��req=requests.delete("��ַ")
     ��req=requests.head("��ַ")
     ��req=requests.options("��ַ")
     
   36.2 get����


