                                     Java


*注：没有提到的与c/c++/c#用法相同

1.cmd不区分大小写
2.cmd中要转变根目录：d: 
3.进入文件夹：cd 文件名  tab自动补全 多次按tab在多种可能间切换
4.退回上一层：cd ..
5.多级文件夹进入：cd 传智播客\05授课视频\JavaEE双元视频
6.一次回到根路径：cd \
7.显示目录列表：dir 
   7.1）数字代表大小，没有大小的显示dir
   7.2）两个点代表上一层
8.清屏：cls
9.退出：exit
10.JRE是Java运行的环境，包含JVM和运行所需要的核心库
11.JDK是Java程序开发工具包，包含JRE和开发人员使用的工具。
12.如果要运行一个已有的Java程序，只要JRE就行
但是如果要开发一个全新的Java程序，就需要安装JDK

13.第一个java程序

   public class HelloWord{
	//第二行的内容是万年不变的固定写法，代表main方法
	//这一行代表程序执行的起点
	public static void main(String[] args)
	{
           //第三行代表打印输出语句
           System.out.println("hellow,world");
	   System.out.println(-500);
	   System.out.println(-2.5);
	}
   }
  //这是一行注释信息//单行注释
  /*多行注释*/
  //第一行的第三个单词必须和所在的文件名称完全一致，大小写也要一样
  //public class后面代表定义一个类的名称，类是Java当中所有元代码的基本组织单位


14.输出单字符并不能有空格，也不能有超过一个字符的字符
15.空常量不能直接用来打印输出（null）
16.基本数据类型
   1）整数型：byte    short    int    long
   2）浮点型：float   double
   3）字符型：char
   4）布尔型：boolean
17.引用数据类型：字符串、数组、类、接口、Lambda
18.字符串不是基本类型，而是引用类型
19.浮点型可能只是一个近似值，而非精确的值
20.数组范围与字节数不一定相关，例如float数据范围比long更广泛，float是4字节，long是8字节
21.浮点数默认类型是double。整数类型默认是int。用float后面加F，long加L
   System.out.println(40F);
22.没有进行赋值的变量，不能直接使用
23.作用域：从定义变量的一行开始，一直到直接所属的大括号结束为止。
24.可以通过一条语句创建多个变量
25.java中使用+  -  *  /  %  ++  -- 运算符，无论怎么计算，也不会得到小鼠
26.类型转换
   1）自动转换 数据范围从小到大
   2）强制类型转换
     2.1）例如：int i = (int)1.5;
     2.2）并不会四舍五入，而是丢掉所有小数
     2.3）boolean类型不能发生数据类型转换
27.一旦运算当中有不同类型的数据，那么结果讲会是数据类型范围大的那种
28.public class string{
    public static void main(String[] args){
     String str1="hellow";
     System.out.println(str1);
     System.out.println(str1+"world");
     }
   }
29.对于数值来说，加法就是加法
30.对于字符char来说，在自诉案之前，会被提升为int，然后再计算。
31.对于字符串String（不是关键字）而说，加号代表字符串链接操作，
任何数据类型和字符串进行链接时，结果都会变成字符串
32.三目运算符的数据类型必须相同

33.方法的定义格式：
   修饰符  返回值类型  方法名 （参数列表）
  {
        代码...
	return ;
   }

   方法调用：方法名()
34.修饰符：目前固定写法：public static
   返回值类型：目前固定写法：void
   一个例子：
   public class demo{
      public static void main(String[] args){
         seller();
         cook();
      }

      //小商贩
      public static void seller()
      {
        System.out.println("吆喝");
      }

      public static void cook()
      {
          System.out.printlin("吃");
      }

   }
   34.1）方法定义的先后顺序无所谓
   34.2）方法的定义不能产生嵌套包含关系



35.对于byte/short/char三种类型而言，如果右侧赋值的数值美誉超过范围，
那么Javac编译器将会自动隐含的为我们补上一个强转，如果超过，则报错
   35.1）short a=5;
         short b=8;
         short result=a+b;//会报错，不能这样写
         short result=5+8;//不会报错
   35.2）在给变量进行赋值的时候，如果右侧的表达式中全是常量，没有任何变量，
那么编译器javac会直接将若干个常量表达式计算得到结果。
short result=5+8；等号右边全是常量，没有任何变量参与运算
编译之后，得到的.class字节码文件中相当于【直接就是】：short result=13；
这称为"编译器的常量优化"
但是：一旦表达式中有变量参与，那么就不能进行这种优化


36.switch：小括号中可以是基本数据类型：byte\short\char\int
           也可以用引用数据类型：string字符串、enum枚举

37.while 循环的扩展格式
   while(条件判断){
       循环体;
       步进语句;

   }

38.方法可以打印调用：System.out.println(sum(10.20));
   System.out.println("the result is:"+number);
   38.1）方法应该定义在类中，但是不能在方法中再定义方法
   38.2）对于一个void没有返回值的方法，不能写return后面的返回值，只能写return自己。
   38.3）对于方法当中最后一行的return可以省略不写
   38.4）一个方法可以有多个return语句，但是必须保证同时只有一个会被执行
   
39.方法重载
   39.1）相关因素：
      39.1.1）参数个数不同
      39.1.2）参数类型不同
      39.1.3）参数的多类型顺序不同
   39.2）无关因素
      39.2.1）参数名称
      39.2.2）返回值类型

40.数组的初始化有两种，一种是动态初始化（指定长度）
      数据类型[] 数组名称=new 数据类型[数组长度];
   一种是静态初始化（指定内容）
      int[] array=new int[]{5,15,23,34};
      省略格式：
        数据类型[] 数组名称={元素1，元素2....}；
      静态初始化没有直接指定长度，但是会自动推算得到长度
      静态初始化标准格式可以拆分成两个步骤
        int[] array;
        array=new int[] {11,12,13};

41.使用动态初始化数组的时候，其中的元素将会自动拥有一个默认值。
   如果是整数类型，默认为0
   如果是浮点数类型，默认为0.0
   如果是字符类型，默认为'\u0000'
   如果是布尔类型，默认为false
   如果是引用类型，默认为null
   静态初始化其实也有初始值，只是系统马上将默认值替换成了大括号中的具体数值。



42.java内存需要分为五个部分
    42.1）栈（stack）
          存放的都是方法中的局部变量，方法的运行一定要在栈中运行
          局部变量：方法的参数，或者是方法{}内部的变量
          作用域：一旦超出作用域，立即从栈内存中消失
    42.2）堆（heap）：凡是new出来的东西，都在堆中
          内存中有一个地址值：16进制
          堆内存里面的数据，都有默认值，规则：
             如果是整数：默认为0
             如果是浮点数类型：默认为0.0
             如果是字符类型：默认为'\u0000'
             如果是布尔类型：默认为false
             如果是引用类型：默认为null
    42.3）方法区（method area）：存储.class相关信息，包含方法的信息
    42.4）本地方法栈（native method stack）：与操作系统有关
    42.5）寄存器（pc register）：与cpu有关


43.int[] arraya={0,10,20};
   int[] arrayb=arraya;
   arrayb和arraya的值一样，数组名为地址
   a与b是同地址，所以b改变a也会改变，a改变b也会改变


44.所有的引用类型变量，都可以赋值为一个null值，但是代表其中什么都没有
   数组必须进行new初始化才能使用其中的元素
   如果值赋值了一个null，没有new创建
   那么将会发生，空指针异常，nullpointexception

45.获取数组长度：数组名.length，将会得到一个int类型的数字

46.一个方法可以有0、1、多个参数，但是只能有0或者1个返回值，不能有多个返回值
   如果希望一个方法当中产生了多个结果数据进行返回，可以将数组作为返回值类型
   public class demo{
     public static void main(String[] args){
       int[] result=calculate(10,20,30);
       System.out.println("total"+result[0]);
     }

     public static int[] calculate(int a,int b,int c){
       int sum=a+b+c;
       int avg=sum/3;
       int[] array={sum,avg};

       return array;
     }
 
   }
   //返回的其实还是数组的地址


47.面向对象
   面向过程时数组的输出
     for(int i=0;i<array.length;i++)
        System.out.println(array[i]);
   面向对象时输出数组
     System.out.println(Arrays.toString(array)); 

48.定义一个类有两个组成部分，一个是属性（是什么）一个是行为（能做什么）

49.导包：import 包名称.类名称
   import cn.itcast.day06.demo01.Student;
   对于和当前类属于同一个包的情况，导包语句可以不写

50.当一个对象作为参数，传递到方法当中时，实际上传递进去的是对象的地址值
51.不赋值的局部变量不能用
52.局部变量：随着方法进栈而生，随着方法出栈而消失
   成员变量：随着对象创建而生，随着对象被回收而消失 
53.用private关键字将需要保护的成员变量进行修饰
   一旦使用那个了private关键字，在本类中仍然可以随意访问，但是超出本类的范围
   就不能再直接访问（不能直接点出来）
   例：
     public class Person{
         String name;
         private int age;

         public void show(){
             System.out.println("my name is"+name,"age"+age);

         }
         
         public void setAge(int number){
             age=number;
         }

         public int getAge()
         {
             return age;

         }

     }


     对于布尔类型的变量，get方法一定要写成isXxx的形式，而setXxx规则不变
     

54.当方法的局部变量和类的成员变量重名的时候，根据就近原则，优先使用局部变量
   如果访问类的成员变量，需要使用：this.成员变量名
   成员变量写，局部变量不写

55.构造方法
   public  类名称(参数类型 参数名称)
  {
      方法体
  }
     55.1）构造方法的名称必须和所在类名称完全一致，包括大小写
     55.2）构造方法不需要写返回值类型，连void都不需要写
     55.3）构造方法不能return一个返回值
     55.4）如果没有构造方法，会有默认构造方法
     55.5）构造方法可以重载

56.一个标准的类通常要满足以下四个组成部分
     56.1）所有的成员变量都要使用private关键字修饰
     56.2）为每一个成员变量编写一对儿getter/setter方法
     56.3）编写一个无参的构造方法
     56.4）编写一个全参的构造方法
   一个标准类也叫做java bean  
   写完成员变量，自动生成另外三个：code（idea），generate
                 快捷键：alt+insert
   按住shift，都选中

57.键盘输入类
     Scanner
     57.1）引用类型的一般使用步骤
         57.1.1）导包
                 import 包路径.类名称；
                 如果需要使用的目标类，和当前类位于同一个包下，则可以省略导包语句不写
                 只有java.lang包下内容不需要导包
         57.1.2）创建
                 类名称 对象名 = new 类名称（）；
         57.1.3）使用
                 对象名.成员方法（） 

     57.2）import java.util.Scanner;//导包
           
           public class demo01scanner{
              public static void main(String[] args){
                 //创建
                 Scanner sc=new Scanner(System.in);
                 //从键盘进行输入
                 //获取键盘输入的一个int数字，sc.nextInt();
                 //获取键盘输入的一个字符串：String str=sc.next();
                 int num = sc.nextInt();
                 System.out.println("输入的int数字是："+num);

                 String str=sc.next();
                 System.out.println("输入的字符串是："+str);

              }
           }

     57.3）匿名对象
          int num=new Scanner(System.in).nextInt();
          System.out.println("输入的是："+num);
          //使用匿名对象进行传参
          //main 中
          methodParam(new Scanner(System.in));
          //方法中
          public static void methodParam(Scanner sc)
          {
              int num=sc.nextInt();
              System.out.println("输入的是："+num);
          }
          //或者
          public static Scanner methodReturn()
          {
              return new Scanner(System.in);  
          }


58.随机数
     58.1）导包
          import java.util.Random;
     58.2）创建
          Random r=new Randow();
     58.3）使用
          int num=r.nextInt();//int所有的范围，有正有负都可以
          //参数代表范围，左闭右开区间
          //如int num = r.nextInt(3)，范围是：[0，3）
          //要想n=5，取[1，5]，只能r.nextInt(n)+1，不能nextInt（n+1）；
          import java.util.Random;
          import java.util.Scanner;

          class random{
             public static void main(String[] args){
               Random r=new Random();
               int num= r.nextInt(100)+1;
               Scanner sc=new Scanner(System.in);
               int input=0;

               while(true){
                  System.out.println("please input one number");
                  input=sc.nextInt();
                  if(input==num)
                {
                   System.out.println("right");
                   return;
                }

                  else if(input>num)
                {
                   System.out.println("too large"); 
                 }else

                {
                  System.out.println("too small");
                 }

             }

            }
          }


59.泛型集合
     import java.util.ArrayList;
     public class arraylist{
        public static void main(String[] args)
        {
            //泛型只能是引用类型，不能是基本类型
            ArrayList<String> list = new ArrayList<>();
            //从jdk 1.7开始，右侧尖括号内部可以不写内容，但是本身还是要写
            //从jdk 8开始 不需要配置classpass环境变量
            //对于arraylist集合来说，直接打印得到的不是地址值，而是内容
            //如果内容是空，那么得到的是空的中括号[]
            list.add("Akutagawa Ryunosuke");
            list.add("Daizai Osamu");
            list.add("JunYear Prisoner");
            public boolean add(E e);向集合中添加元素，参数的类型和泛型一致
            public E get(int index);从集合中获取元素，参数是索引编号，返回值是对应位置元素
            public E remove(int index)；从集合中删除元素，参数是索引编号，返回值就是被删除掉的元素
            public int size();获取集合的长度

            //添加
            boolean success = list.add("five");
            System.out.println(list);
            System.out.println("if add success "+success);
            String whoRemovved=list.remove(4);
            for (int i=0;i<list.size();i++)
            {
                System.out.println(list.get(i));
            }
        }
     }


     59.2）集合中存储基本数据类型的方法
           必须使用基本类型对应的"包装类"
           包装类（引用类型，位于java.long包下）
           byte     Byte
           short    Short
           int      Integer
           long     Long
           float    Float
           double   Double
           char     Character
           boolean  Boolean

           ArrayList<Integer> list = new ArrayList<>();
           list.add(100);
           //把integer当作int用
           //从jdk1.5+开始，支持自动装箱，自动拆箱
           //自动装箱：基本类型--->包装类型


60.使用例子           
stu.java           
import java.util.ArrayList;

class stu
{
   public static void main(String[] main)
   {
      ArrayList<Student>list = new ArrayList<>();

      Student one=new Student("zhanghao",20);
      Student two=new Student("lihan",20);
      Student three=new Student("yangwenbo",20);
      Student four=new Student("liuyachao",20);
      list.add(one);
      list.add(two);
      list.add(three);
      list.add(four);

      for(int i=0;i<list.size();i++)
      {
          Student stu=list.get(i);
          System.out.println("name"+stu.getName()+"  age"+stu.getAge());
      }
   }
}


Student.java
  public class Student
   {
      private String name;
      private int age;
      public Student(){}
      public Student(String name,int age)
      {
         this.name=name;
         this.age=age;
      }

      public String getName()
      {
         return name;
      }

      public void setName(String name)
      {
         this.name=name;
      }

      public int getAge()
      {
         return age; 
      }

      public void setAge(int age)
      {
         this.age=age;
      }

   }


          
61.字符串
    61.1）字符串是常量，不可更改，因此可以共享使用
          字符串效果上相当于是char[]字符数组，但底层原理是byte[]字节数组
          创建字符串的方法有3+1种：三种构造方法，一种直接创建
          61.1.1）public String()
          61.1.2）public String(char[] array):根据字符数组的内容，来创建对应的字符串
          61.1.3）public String(byte[] array):根据字节数组的内容，来创建对应的字符串
          61.1.4）直接创建
     
    61.2）使用空构造
          String str1=new String();//小括号留空，说明什么都没有

    61.3）使用字符数组创建字符串
          char[] array={'c','b','a'};
          String str2=new String(array);
          //str2=cba
    61.4）字节数组表示
          byte[] array={97,98,99}//a,b,c
         String str3=new String(array);
    61.5）直接创建
          String str4 = "hello";
    61.6）不管有没有new，直接写上双引号，就是字符串对象   
    61.7）引用类型==比较的是地址值，equals比较的才是内容
    61.8）双引号直接写的字符串在常量池中，new的不在池中
    61.9）public boolean equals(Object obj):参数可以是任意对象，只有参数是一个字符串并且
                                            内容相同时才会给true
           任何对象都能用object进行接收
          String str1="hellow";
          String str2="hellow"
          char[] charArray={'h','e','l','l','o','w'};
          String str3=new String(charArray);

          System.out.println(str1.equals(str2));//true
          System.out.println(str2.equals(str3));//true
          System.out.println(str3.equals("hellow"));//true
          System.out.println("hellow".equals(str1));//true

          equals方法具有对称性，也就是a.qeuals(b)和b.equals(a)效果一样
          推荐使用："abc".equals(str)  不推荐:str.equals("abc")
          
          equalsIgnoreCase(strb);//忽略大小写 
    61.10）public String concat(String str):将当前字符串和参数字符串拼接成功并返回新的字符串
    61.11）public char charAt(int index):获取指定索引位置的单个字符（索引从0开始）
    61.12）public int indexOf(String str):查找参数字符串在本字符串当中首次出现的索引位置，如果没有就返回-1

    61.13）截取字符串
           public String substring(int index);
           //截取从参数位置一直到字符串末尾，返回新字符串
           public String substring(int begin,int end);
           //截取从begin开始，一直到end结束，中间的字符串
           //是左闭右开区间，[begin，end)，包含左边不包含右边

    61.14）转换字符串
           public char[] toCharArray();
           //将当前字符串拆分成字符数组作为返回值
           public byte[] getBytes();
           //获得当前字符串底层的字节数组
           public String replace(CharSequence oldString,CharSequence newString);
           //将所有出现的老字符穿替换成为新的字符串，返回替换之后的结果


    61.15）分割字符串
           public String[] split(String regex);
           //按照参数的规则，将字符串切分成各个若干部分
           //例如
           //split方法的参数其实是一个"正则表达式"
           //如果按照英文句点"."进行分割，必须写"\\."
           String str1="aaa,bbb,ccc";
           String[] array1=str1.split(",");


62.static 关键字
    62.1）一旦用了static关键字，那么这样的内容不再属于对象自己，而是属于类的，
          所以凡是本类的对象，都共享同一份
    62.2）一旦使用static修饰成员方法，那么这就成为了静态方法，静态方法不属于对象，属于类
    62.3）如果没有static关键字，那么必须先创建对象，然后通过对象才能使用它
    62.4）对于静态方法来说，可以通过对象名进行调用，也可以直接通过类名称来调用
    62.5）对于本类当中的静态方法，可以省略类名称
    62.6）静态只能直接访问静态，不能直接访问非静态
    62.7）在内存中现有的静态内容，后有的非静态内容
    62.8）静态方法当中不能用this。this 代表当前对象，通过谁调用的方法，谁就是当前对象
    62.9）根据类名称访问静态成员变量的时候，全程和对象没有关系，只和类有关系
    62.10）静态代码块的格式是：
           public class 类名称{
               static {
                   //静态代码块的内容
               }
           }

           
           //特点：当第一次用到本类时，静态代码块执行唯一的一次
           public class Person{
               static{
                   System.out.println("静态代码块执行!");
               }
           }

    62.11）静态内容总是优先于非静态，所以静态代码块比构造方法先执行
    62.12）静态代码的典型用途：用来一次性地对静态成员变量进行赋值


63.Arrays库
    63.1）java.util.Arrays是一个与数组相关的工具类，里面提供了大量的静态方法，用来实现数组常见操作
    63.2）public static String toString(数组)
    //将参数数组编程字符串（按照默认格式：[元素1，元素2...]）
    63.3）public static void sort(数组)
    //按照升序从小到大排序，如果是字符串，按着字母升序
    //如果是自定义的类型，那么这个自定义的类型需要有Comparable或者Comparator接口支持
    //
     




