                                    Linux 操作系统

44725937+JunYearPrisoner@users.noreply.github.com

1.学习方向：linux运维工程师、Linux嵌入式工程师
linux下项目开发：JavaEE、大数据、Python、PHP、C/C++


2.虚拟机的网络链接的三种形式的说明
  1）桥连接：Linux可以和其它系统通讯。但是可能造成ip冲突
  2）NAT：网络地址转换方式：Linux可以访问外网，不会造成ip冲突
  3）主机模式：你的Linux是一个读理的主机，不能访问外网


3.CentOS的终端使用和联网
  1）右键->使用终端打开
    1.1）更改终端背景色字体等：编辑->侧写首选项
  2）联网：点击右上侧两个计算机的平面，选择启用eth0


4.Windows操作系统与centos共享文件夹
  1）实现功能：
    1.1）可以直接粘贴命令在Windows和centos系统之间
    1.2）可以设置Windows和centos的共享文件夹
  2）安装vmtools工具
    1.1）虚拟机->vmtools
    1.2）tar -zxvf 解压指令
    1.3）按tab自动补全文件名
    1.4）重启指令：reboot
    2.1）虚拟机->设置->选项->文件共享->虚拟机中计算机->文件系统->mnt

 
5.Linux的根目录只有一个：/


6.Linux的文件系统采用级层式的树状目录结构，在此结构的最上层是根目录“/”
然后在此目录下再创建其它的目录。
  1）/dev管理设备
  2）/media
  3）/bin（重点）（/usr/bin，/usr/local/bin）
     是Binary的缩写，这个目录存放着最经常使用的命令，如拷贝啊，删除啊
  4）/sbin（/usr/sbin、/usr/local/sbin）
     s是super user的意思，这里存放的是系统管理员使用的系统管理程序
  5）home（重点）
     存放普通用户的主目录，在Linux中每个用户都有一个自己的目录，一般
改目录名是以用户的账号命名的
  6）/root（重点）
     改目录为系统管理员，也称作超级权限者用户主目录
  7）/lib
     系统开机所需要的最基本的动态链接共享库，其作用类似于Windows里的dll文件
几乎所有的应用程序都需要用到这些共享库
  8）/lost+found
     这个目录一般情况是空的，当系统非正常关机后，就存放一些文件
  9）/etc（重点）
     所有的系统管理所需要的配置文件和子目录my.colf
  10）/usr（重点）
     这是一个非常重要的目录，用户的应用程序和文件都会放在这个目录下，类似于
Windows下的program files目录
  11）/boot（重点）
     存放的是启动Linux时使用的一些核心文件，包括一些链接文件以及镜像文件
  12）/proc（不要动
     虚拟目录，它是系统内存的映射，访问这个目录来获取系统信息
  13）/srv（不要动
     service缩写，改目录存放一些服务器启动之后需要提取的数据
  14）/sys（不要动
     Linux2.6内核的一个很大变化，安装了2.6内核中新出现的一个文件系统
  15）/tmp
     这个目录用来存放一些临时文件 
  16）/dev
     类似于Windows的设备管理器，把所有的硬件用文件的形式存储
  17）/media（重点）
     Linux系统会自动识别一些设备，例如u盘、光驱单独，当识别后，Linux会把识
别的设备挂载到这个目录下
  18）/mnt（重点）
     系统提供该目录时为了让用户临时挂在别的文件系统的，我们可以将外部的存储
挂载在/mnt/上，然后进入该目录就可以查看里面的内容了
  19）/opt
     这是给主机额外安装软件所摆放的目录。如安装ORACLE数据库就可以放到该目录下。
默认为空。
  20）/usr/local（重点）
     这是另一个给主机额外安装软件所安装的目录。一般时通过编译源码的方式安装
的程序
  21）/var（重点）
     这个目录中存放着不断扩充着的东西，习惯将经常被修改的目录放在这个目录下。
包括各种日志文件。
  22）/selinux[secur-enhanced linux]
     selinux时一种安全子系统，它能控制程序只能访问特定文件



7.远程登陆到Linux
  1）xshell：远程登陆到Linux的软件
  2）远程上传下载：xftp5 需要Linux开启sshd服务
  3）192.168.3.128


8.vi/vim
  1）所有的Linux系统都会内建vi文本编辑器
  2）vim具有程序编辑的能力，可以主动的以字体颜色辨别语法的正确性，
方便程序设计。代码补充、编译及错误跳转等方便编程的功能特别丰富。
  3）vi/vim的三种模式
     3.1）正常模式
        3.1.1）可以使用快捷键，上下左右可以移动光标，使用删除字符或删除整行
        来处理文档内容，也可以用复制粘贴来处理数据
     3.2）插入模式
        3.2.1）可以输入内容，按下i，I，o，O，a，A，r，R都可以进入
     3.3）命令行模式
        3.3.1）可以提供相关指令，完成读取，存储，替换，离开vim，显示行号等
  4）编辑模式退回正常模式：esc
  5）命令模式退回正常模式：esc  命令行下:wq退出保存 :q退出不保存 :q!强制退出
  6）正常模式进去命令模式:或者/
  7）vi/vim快捷键
    7.1）拷贝当行，yy，拷贝当前向下的5行，5yy，并粘贴
    7.2）删除当行，dd，删除当前向下的5行，5dd
    7.3）在文件中查找某个单词[命令行下/关键字，回车 查找，输入n就是查找下一个]
    7.4）设置文件的行号，取消文件的行号[命令行下:set nu和:set noun]
    7.5）编辑/etc/profile文件，使用快捷键到底文档的末行[G]和首行[gg]
    7.6）在一个文件中输入"hello"，然后撤销这个动作 u
    7.7）编辑/etc/profile文件，讲光标移动到20行 shift+g
    7.8）i 写入模式、i插入之前、a插入之后、A行尾插入、
         I行首插入、o下行插入、O上行插入
    7.9）x 删除光标后一个字符
    7.10）d + ←→删除光标←→字符（d +3←）、dd删除一行（其实是剪切，p粘贴）
    7.11）y+ ←→复制光标←→字符 （y+3←）
    7.12）c 删除并进入写入模式、w 光标向下移动一个词、cw删除一个词并进入写入模式、
         b光标到上一个词 、ciw词中删除一个词并进入写入模式，yi
    7.13）f 找词
    7.14）/ 搜索、n下 N上
    7.15）【y i c d f 】
    7.16）esc 回到正常模式
    7.17）：w保存
    7.18）：q退出vim
    7.19）：source $MYVIMRC 刷新vim
    7.20）jkhl上下左右
    7.21）：split 上下分屏 、：vsplit 左右分屏 Q退出
    7.22）~/.vim/vimrc
    7.23）noremap a b a键改b键
    7.24）map a b a键改b键
    7.25）syntax on 打开高亮
    7.26）set number 显示行号
    7.27）set wildmenu   ：命令补全
    7.28）set hlsearch  /搜索高亮
    7.29）set incsearch  一面输入一面高亮
    

9.关机&重启命令
  9.1）shutdown
      9.1.1）shutdown -h now :表示立即关机
      9.1.2）shutdown -h 1:一分钟后关机
      9.1.3）shutdown -r now:立刻重启
  9.2）halt
      就是直接使用，效果等价于关机
  9.3）reboot
      重启系统
  9.4）sync
      把内存的数据同步到磁盘


10.登陆和注销
   10.1）尽量少用root账号登陆，因为权限最大。可以以普通用户登陆，登陆后
再用"su-用户名"命令来切换成系统管理员身份
   10.2）在提示符下输入logout即可注销用户
   10.3）logout注销指令在图形运行级别无效，在运行级别3下有效


11.用户
   11.1）用户家目录。/home/目录下有各个创建的用户对应的家目录，当用户登陆时，
会自动进入到自己的家目录。
   11.2）Linux是一个多用户多任务的操作系统，任何一个要使用系统资源的用户，
都必须首先向系统管理员申请一个账号，然后以这个账号的身份进入系统
   11.3）添加用户
       11.3.1）useradd [选项]用户名
       11.3.2）如果没有指定组，会默认创建一个跟用户名同名的组，并且将用户放到这个组中
       11.3.3）cd表示change directory切换目录
       11.3.4）通过useradd -d指定目录 新的用户名
       11.3.5）passwd 用户名 ：修改指定用户的密码
   11.4）删除用户
       11.4.1）userdel 用户名    
       11.4.2）删除用户，但是保留家目录
       11.4.3）删除用户以及用户主目录 userdel -r 用户名
       11.4.4）删除用户时，一般不会将家目录删除掉
   11.5）查询用户信息 id 用户名
       11.5.1）uid 用户的id号   gid用户所在组的id号
   11.6）切换用户
       11.6.1）su -用户名
       11.6.2）从权限高的用户切换到权限低的用户，不需要输入密码，反之需要
       11.6.3）当需要返回到原来的用户时，使用exit指令
   


12.用户组
   12.1）类似于角色，系统可以对有共性的的多个用户进行统一管理
   12.2）增加组 groupadd 组名
   12.3）删除组 groupdel 组名
   12.4）修改用户的组 usermod -g 用户组 用户名



14.用户和组的相关文件
   14.1）/etc/passwd 文件
        用户（user）的配置文件，记录用户的各种信息
        每行的含义：用户名：口令：用户标识码：组标识号：注释性描述：主目录：登陆shell
   14.2）/etc/shadow 文件
        口令配置文件，密码和登陆信息，是加密的
        每行的含义：登录名：加密口令：最后一次修改时间：最小时间间隔：
      最大时间间隔：警告时间：不活动时间：失效时间：标志
        权限不够用vim /etc/shadow打开
   14.3）/etc/group 文件
        组配置文件，记录Linux包含的组信息
        每行含义：组名：口令：组标识号：组内用户列表
 

15.实用指令
   15.1）运行级别：0  关机
                   1  单用户【找回丢失密码】
                   2  多用户状态没有网络服务
                   3  多用户状态有网络服务
                   4  系统为使用保留给用户
                   5  图形界面
                   6  系统重启
         常用运行级别是3和5，要修改默认的运行级别可改文件
         /etc/inittab的id:5:initefault:这一行中的数字
         命令：init[0123456]
     
         系统的运行级别配置文件/etc/inittab
   15.2）centos7中/etc/inittab已经被弃用，需要用systemctl修改用户启动级别
         systemctl get-default 查看当前用户的启动级别
         systemctl set-default multi-user.target启动级别设为3
         systemctl set-default graphical.target启动级别设为5
         tips：centos7只能设为3和5两种模式
   15.3）如何找回root密码
         进入到单用户模式，修改root密码。因为进入单用户模式，root不需要密码就可以登陆
         重启时按enter键，然后按e，选中第二行，再输入e，然后空格1，回车，输入b，就会
     进到单用户模式
   15.4）设置运行级别，Linux运行后直接进入到命令行界面
   15.5）vim/etc/inittab   id:3:initdefault
   


16.帮助指令
   16.1）基本语法 man[命令或配置文件]（文字描述：获得帮助信息）
   16.2）help指令 基本语法 help 命令
   16.3）linux中带.的文件默认不显示
   16.4）按q退出帮助文档
   16.5）



  
10.解压
  1）tar -zxvf 文件名
  2）./xx表示该目录下可执行文件
  3）配置环境
    3.1） G定位到末尾
    3.2）[root@AKtgwPC 桌面]# cd /opt
         [root@AKtgwPC opt]# cd jdk
         jdk1.7.0_79/           jdk-7u79-linux-x64.gz  
         [root@AKtgwPC opt]# cd jdk1.7.0_79/
         [root@AKtgwPC jdk1.7.0_79]# cd  bin/
         [root@AKtgwPC bin]# vim /etc/profile
	 G
         JAVA_HOME=/opt/jdk1.7.0_79
         PATH=/opt/jdk1.7.0_79/bin:$PATH  :代表链接，要把原先路径加进去
    3.3）需要注销用户，环境变量才能见效
    3.4）运行3级别，logout
    3.5）运行5级别
    3.6）
  4）安装tomcat
    4.1）解压:tar -zxvf apache-tomcat-balabala
    4.2）启动tomcat
       4.2.1）需要先进入tomcat的bin目录
       [root@AKtgwPC opt]# ls
       apache-tomcat-7.0.70                        jdk-7u79-linux-x64.gz
       apache-tomcat-7.0.70.tar.gz                 mysql-5.6.14.tar.gz
       eclipse-jee-mars-2-linux-gtk-x86_64.tar.gz  rh
       Hello.class                                 VMwareTools-10.0.5-3228253.tar.gz
       Hello.java                                  vmware-tools-distrib
       jdk1.7.0_79
       [root@AKtgwPC opt]# cd apache-tomcat-7.0.70/bin/
       [root@AKtgwPC bin]# ls
       bootstrap.jar                 daemon.sh         startup.sh
       catalina.bat                  digest.bat        tomcat-juli.jar
       catalina.sh                   digest.sh         tomcat-native.tar.gz
       catalina-tasks.xml            setclasspath.bat  tool-wrapper.bat
       commons-daemon.jar            setclasspath.sh   tool-wrapper.sh
       commons-daemon-native.tar.gz  shutdown.bat      version.bat
       configtest.bat                shutdown.sh       version.sh
       configtest.sh                 startup.bat
      [root@AKtgwPC bin]# ./startup.sh
      Using CATALINA_BASE:   /opt/apache-tomcat-7.0.70
      Using CATALINA_HOME:   /opt/apache-tomcat-7.0.70
      Using CATALINA_TMPDIR: /opt/apache-tomcat-7.0.70/temp
      Using JRE_HOME:        /opt/jdk1.7.0_79
      Using CLASSPATH:       /opt/apache-tomcat-7.0.70/bin/bootstrap.jar:/opt/apache-tomcat-7.0.70/bin/tomcat-juli.jar
      Tomcat started.
      4.2.2）http://localhost:8080/
             使用Linux的本地浏览器是可以访问到的
	     但是如果Windows要想访问到，必须要防火墙放行8080先配置而后重启

[root@AKtgwPC bin]# service iptables status
表格：filter
Chain INPUT (policy ACCEPT)
num  target     prot opt source               destination         
1    ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED 
2    ACCEPT     icmp --  0.0.0.0/0            0.0.0.0/0           
3    ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           
4    ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           state NEW tcp dpt:22 
5    REJECT     all  --  0.0.0.0/0            0.0.0.0/0           reject-with icmp-host-prohibited 

Chain FORWARD (policy ACCEPT)
num  target     prot opt source               destination         
1    REJECT     all  --  0.0.0.0/0            0.0.0.0/0           reject-with icmp-host-prohibited 

Chain OUTPUT (policy ACCEPT)
num  target     prot opt source               destination         

[root@AKtgwPC bin]# vim /etc/sysconfig/iptables
[root@AKtgwPC bin]# service iptables restart
iptables：将链设置为政策 ACCEPT：filter                    [确定]
iptables：清除防火墙规则：                                 [确定]
iptables：正在卸载模块：                                   [确定]
iptables：应用防火墙规则：                                 [确定]
[root@AKtgwPC bin]# service iptables status
表格：filter
Chain INPUT (policy ACCEPT)
num  target     prot opt source               destination         
1    ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED 
2    ACCEPT     icmp --  0.0.0.0/0            0.0.0.0/0           
3    ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           
4    ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           state NEW tcp dpt:8080 
5    ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           state NEW tcp dpt:22 
6    REJECT     all  --  0.0.0.0/0            0.0.0.0/0           reject-with icmp-host-prohibited 

Chain FORWARD (policy ACCEPT)
num  target     prot opt source               destination         
1    REJECT     all  --  0.0.0.0/0            0.0.0.0/0           reject-with icmp-host-prohibited 

Chain OUTPUT (policy ACCEPT)
num  target     prot opt source               destination         

[root@AKtgwPC bin]# 


  vim中的配置
  -A INPUT -m state --state NEW -m tcp -p tcp --dport 8080 -j ACCEPT
  -A INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT
	     
	  
  5）eclipse的安装


11.bash shell环境下，定义本地变量的格式：#s1=hellow  #s2="hellow"
   等号两边不能直接有空格
   定义规则与其它语言相同
   引用值的时候要加一个$符号
   如果值之间有空格，要加一个引号
   双引号引起来的字符串可以有变量
   单引号不可以全部是字符
   z= expr $x + $y #相加
   echo输出
   echo -n输出不换行

   test
   两个数字相等是用eq，字符串相等使用= 或者用-o
   不相等是ne，小于lt，前小于等于后le
   test -e 判断是否存在，存在返回0  而后用echo $?
   -d 存在且为目录
   -f 存在且为文件
   -l 存在且为符号连接
   -r 存在且可读
   -s 存在且长度为0
   -w 存在可写
   -x 存在可执行
   -a 两个条件同时满足为0
   


12.只读#readonly

13.read [-pt] 变量名 
   从键盘中读入
   -p提示信息 ' '
   -t等待时间 

14.显示变量，同时也可以用echo ${变量名}   

15.命令提示符中 PS1=[\u@\h \W]\$ 账户名 主机名 工作目录 账户

16.export 变量名 ，可以将本地变量设置为环境/全局变量

17.$#存储shell中参数的个数
   $?上一个程序的返回值，0表示运行成功，非零有问题
   $[1-n]存储第1-n个
   $*所有参数
   $$运行进程的编号
   $0shell自己的名字
   
18.mkdir 创建目录
   mkdir -p 创建多级目录
   例如：mkdir -p /home/animal/tiger

19.删除目录：rmdir只能删除空目录，如果目录下有东西，无法删除
   要用rm -rf删除 （r，recursion，递归删除）

20.touch：创建文件
   touch 文件名



21.后台进程要是想关闭，只能用kill杀死
   执行文件： bash 文件名

22.流程控制
     22.1）条件语句
          22.1.1）if 语句
                  if <判断命令>;#[]也可以
                  then{命令清单1}
                  else{条件不成立}
                  fi

             1.2）使用if-then-else创建
                  #!/bin/bash
                  #filename:ak
                  echo -n "please input a scoure"
                      read SCORE
                      echo "you input score is $SCORE"
                  if [$SCORE -ge 60 ];
                      then
                         echo -n "Congratulation! You pass the examination."
                  else
                      echo -n "Sorry! You fail the examination"
                  fi
                  echo -n "Press any key to continue!"
                      


          22.1.2）case语句
                  case <变量> in
                      <字符串1>){<命令清单1>};;
                      <字符串2>){命令清单2};;
                      *)
                  exit 11
                  esac
                  #多个语句都符合，则只执行一个
                  #如果都不是，则执行*

              1.2.1）创建一个菜单选择
                  #!/bin/bash
                  #filename za
                  echo _
                  echo "1. Restore"
                  echo "2. Backup"
                  echo "3. Unload"
                  echo
                  #Read and excute the user's selection
                  echo -n "Enter Choise"
                  read CHOICE
                  case '$CHOICE' in
                      1) echo "Restore";;
                      2) echo "Backup";;
                      3) echo "Unload";;
                      *) echo "Sorry $CHOICE is not a valid choice"
                           exit 11
                  esac


     22.2）循环语句
          22.2.1）for i in 1 2 3
                  #循环三次
                  # /*去掉特殊含义，表示*是一个乘号
                  length 可以求字符串的长度
                  `expr $LOOP + 1`#键盘esc下的
                  continue 和 break 同c语言

             2.1.1）例子 求命令行上所有整数
                  #!/bin/bash
                  #filename:ggg
                  sum=0
                  for INT in $*
                  do
                      sum= expr $sum + $INT
                  done
                  echo $sum

     22.3）expr 是一个手工命令行计数器
           下求表达式变量的值，一般用于整数值，也可用于字符串
           格式为：expr Experssion
           （命令读入Experssion参数，计算它的值，然后将结果输出到标准输出）
           
           参数使用规则：
              22.3.1）用空格隔开每个项
              22.3.2）用\ 放在shell 特定的字符前面
              22.3.3）对包含空格和其它特殊字符的字符串都要用引号括起来，

           计算字符串长度：
              22.3.4）# expr length "this is a test"

           增量计算：
              22.3.5）expr在循环中用于增量计算，先将变量初始化为0，然后循环增加1，
                      反引号（esc下）的用法为命令替代。
                      #LOOP=0
                      #LOOP=`expr $LOOP + 1`
     
     22.4）控制流while循环
           while<判别命令>
           do<命令>
           done
           当<判别命令>返回0时，（对于test命令，其后就是表达式成立），
           则执行do后的命令清单，然后再重作循环；否则，退出循环

           while控制经常与前述的shift命令结合使用

           22.4.1）编写一个exist，用于判别其后用参数方法指定的一系列文件是否存在
                   #!/bin/bash
                   while test -n "$1"   #"$1"两边的引号不能省略
                   do
                       if test -e $1
                       then echo "$1 exist"
                       else echo "$1 not exist"
                       fi
                       shift
                   done

           22.4.2）加从0开始的五个偶数
                   #!/bin/bash
                   loopcount=0
                   result=0
                   while [$!loopcount -lt 5]  #也可以写成while test $loopcount -lt 5
                   do
                       increment=`expr $loopcount \* 2`
                       result=`expr $result + $increment`
                       loopcount=`expr $loopcount + 1`
                   done
                   echo "result is $result"

           22.4.3）创建一个计算1到5的平方的shell程序
                   #!/bin/bash
                   #filename:zx
                   int=1
                   while [ $int -le 5 ]
                   do
                       sq=`expr $int \* $int`
                       echo $sq
                       int=`expr $int + 1`
                   done
                   echo "job completed"

              



23.here文本，使用here文本，可以方便地将一些需要进行用户交互的命令放入到shell脚本里
     23.1）例如，编写一个shell脚本erase_first_line(efl)，并再置顶文本本舰中删除第一行
           ##!/bin/bash
           #vi $1 <<!
           #dd:wq!
           #!
           

24.函数 
     23.1）所有函数在使用前必须定义，要将函数方在程序开始的地方
     23.2）Time()
           {
               echo "the system time now is `date`"
           }

     23.3）例子：获取函数的返回值
           #!/bin/bash
           #filename:text3
           func_test()
           {
              if test -z "$1"
              then
                  echo "none input"
                  return 0
              else
                  echo "$1"
                  return 1
              fi

           }
           
           func_test $1
           echo $?
           
     23.4）函数的调用，只需要使用函数名，例如写一个完整的脚本time
           #!/bin/bash
           #function Time
           Time()
           {
               TM=`date`
               echo "the system time now is ${TM}"
           }

           echo "now is gonging to the function time"
           Time
           echo "back from the fuction Time"
            

     23.5）less 可以翻页显示
           for fname in `ls -R $file` ：ls 显示文件信息
                                        -R 显示子目录/递归显示
                                        结果里面的每一项都会执行一遍
           
           shift 2 左移两位
           local 局部变量
           \ 逃逸字符
           export 局部变量变全局变量
           declare -r 声明一个只读变量


24.网络配置
     24.1）ifconfig 只能暂时使用，下次使用无效
           ifconfig ech0 192.168.0.5 up #临时设置更改ip地址
     24.2）openssh 支持使用客户端服务的工具（没有图形化界面）
               ssh + ip地址
           vnc 图形化的服务器配置
           nps 网络文件系统 可以共享 相当于一个网盘
           web 服务器配置 可以设置一个站点，通过ip地址访问
     24.3）scp 远程复制  
     24.4）
     grep过滤 显示出带xxx的结果

     nfs recbind 要打开才能共享
     service recbind start

     挂载
     mount -t nfs ip名:/myshare 目录（挂载点）
     要保证网络是通的

     status查看状态                                   







