                    git 与GitHub

1.git命令行操作
   1.1本地库初始化
      1.1.1命令：git init
         11750@DESKTOP-URTIHVE MINGW64 /d/Git/CeShi
         $ git init
         Initialized empty Git repository in D:/Git/CeShi/.git/

         11750@DESKTOP-URTIHVE MINGW64 /d/Git/CeShi (master)
         $ ls -lA
         total 4
         drwxr-xr-x 1 11750 197609 0  6月 27 14:04 #.git

         11750@DESKTOP-URTIHVE MINGW64 /d/Git/CeShi (master)
         $ ll .git/
         total 7
        -rw-r--r-- 1 11750 197609 130  6月 27 14:04 config
        -rw-r--r-- 1 11750 197609  73  6月 27 14:04 description
        -rw-r--r-- 1 11750 197609  23  6月 27 14:04 HEAD
        -drwxr-xr-x 1 11750 197609   0  6月 27 14:04 #hooks
        -drwxr-xr-x 1 11750 197609   0  6月 27 14:04 #info
        -drwxr-xr-x 1 11750 197609   0  6月 27 14:04 #objects
        -drwxr-xr-x 1 11750 197609   0  6月 27 14:04 #refs
        #(注：这里的#和#所在的行的-都是为了借高亮)

      1.1.2 init 初始化后会新建一个隐藏目录.git，里面会放置一些配置文件
      1.1.3 .git目录中存放的是本地库相关的子目录和文件，不要删除，也不要胡乱修改

2.设置签名
   2.1形式
      用户名：tzz
      Email地址：goodMorning@AKtgw.com
      作用：区分不同开发人员的身份
   
   2.2级别：
      ·项目级别/仓库级别：仅在当前项目生效
      ·系统用户级别：登录当前操作系统的用户范围
      优先级：如果都设置的话，按照就近原则生效，会使用项目级别不会使用系统用户
      !:而且必有其一，两个都没有是不允许的

   2.3 git config：设置项目级别
         ·git congit user.name tzz
         ·git congit user.email goodMorning@AKtgw.com
       git config --global ：设置系统用户级别
         ·git config --global user.name tzz_glb 
         ·git config --global user.email goodMorning_glb@AKtgw.com

   2.4这些被设置到.git/condig目录下，使用 cat .git/config查看

3.提交
   3.1提交：git add 文件名.文件类型
       ·这里提前避一下雷
       ·通过你的客户端命令行修改换行设置，输入
          ·git config --global core.autocrlf false
          ·git config --global core.safecrlf true
          https://blog.csdn.net/qq_42672770/article/details/86557593

       ·git config --global core.editor gvim
       ·设置编辑器位vim
       
   3.2撤回提交：git rm --cached 文件名.文件类型  
   3.3从暂存区提交到本地库
      git commit 文件名.文件类型
      此时再用git status查看会提示
        on branch master
        nothing to commit,working tree clean

      3.3.2 可以使用git commit -m "修改内容" 文件名.文件类型
        不进入编辑器进行提交
        
      3.3.3根提交只能有一个     

4.基本操作
   工作区：写代码
   暂存区：临时存储
   本地库：例时版本
   4.1状态查看操作
      git status
      查看工作区、暂存区状态

   4.2添加操作
      git add
      将工作区的"修改/新建"添加到暂存区

   4.3提交操作
      git commit -m "修改内容" 
      将暂存区的内容提交到本地库

   4.4版本记录
      git log
      如果记录过多一屏放不下，按空格键进行下一页切换，b向上
      ps：和Linux中less命令一样
      按q退出日志
      git log --pretty=oneline #以一行显示每条日志，哈希值显示全部
      git log --online #哈希值显示部分
      git reflog(显示步数)

   4.5基于索引值的后退  
      git reset --hard 哈希值(由reflog显示出的)
      基于索引值的前进
      git reset --hard 哈希值(由reflog显示出的)

   4.6基于^和~的后退
      git reset --hard HEAD^(进入到上一个版本)
      按异或符号的个数去回退 一个回退一个 两个回退两个
      tail：显示文本的最后n行，如：tail -n 3 文件名.文件格式
      git log --oneline 只显示后边的版本，不显示前面的版本
      或者可以用~3表示回退三步 写法与上面相同

5.git文档的查看
   git help 具体命令

6.reset三个参数的对比   
   6.1 soft 仅仅在本地库移动head指针
       不会修改本地文件
   6.2  mixed 
       ·在本地库移动head指针
       ·重置暂存区
        不会修改本地文件
   6.3 ·在本地库移动head指针
       ·重置暂存区
       ·重置工作也

7.文件的删除
   7.1删除
      rm 文件名.文件类型
      如果先add了话
      使用git status查看，会有个红字的提示
      再次使用git add，就会记录删除
      使用git commit提交 在历史记录中就会记载
      就可以使用reset回到未被删除的时候
     
   7.2删除并找回
      前提：删除前，文件存在时的状态提交到了本地库
      操作：git reset --hard[指针位置]
            指针位置：历史记录或当期位置
              ·已提交到本地库：指针位置指向历史记录
              ·尚未提交到本地库：指针位置使用HEAD

8.文件的比较
   当修改完一个文件后，可以使用diff命令进行查看修改前后的比较
   git diff 文件名.文件类型
   但是如果add了之后再diff
   就不会有信息了
   而如果加上HEAD 就会有了
   git diff HEAD 文件名.文件类型

9.分支管理
   9.1 分支介绍：
       新分支（习惯以feature_命名）是从主干复制过来的，也即开始时新分支与主干内容相同
       各个分支在开发过程中是相互独立的
       分支对主干（master）没有任何影响
       分支也可以合并为主干，对主干而言是大版本升级
       当主干有bug，一般创建hot_fix分支去修复再合并，一般不停服务器所以这样干
   
   9.2 分支查看
       git branch -v

   9.3 分支建立
       git branch 分支名

   9.4 分支切换
       git checkout 分支名

   9.5 合并分支
       必须在接受合并的那个分支下（主分支）
       然后使用git merge 分支名（hot_fix分支）

   9.6 分支冲突
       当出现冲突后，手动修改
       然后重新add，再commit，commit时不需要加文件名

10.提交
   10.1 查看地址别名
       git remote -v

   10.2 给地址取别名
       git remote add 别名 地址

   10.3 推送
       git push 别名 分支名
       从本地库上传远程库

   10.4 抓取
       git fetch 别名 分支名
       从远程库上传本地库，但是并不会改本地库文件
       git checkout origin/main 进入到这里查看
       然后用 git merge origin/main(别名/分支名)将远程库本地库合并
       
   10.5 提交冲突
       如果本地库非最新版提交时会提交失败，
       这时pull一下，然后和手动修改冲突文件，再add，再commit，再push
       提交依旧不带文件名

       另外：pull=fetch+merge
