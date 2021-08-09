                                         Unity

1.scene          场景编辑窗口
  game           游戏运行窗口
  hierarchy      场景物体 列表窗口
  project        项目资源 列表窗口
  inspector      属性编辑 列表窗口


2.File         文件菜单
  Edit         编辑菜单
  Assets       资源菜单
  GameObject   物体菜单
  Component    组件菜单
  Window       窗口菜单
  Help         帮助菜单

 
3.scene窗口上方有四个按键可以同过qwer进行切换


4.hierarchy与场景搭建

   4.1）基本组件
      4.1.1)camera 表示用户所看到的视野，又下方小框框中与game中视野是相同的
      4.1.2）inspector中death表示camera的优先级
            death越大，优先级越高
   4.2）灯光组件
   4.3）物体组件
   4.4）其它组件
   4.5）层级关系与运用
   4.6）场景搭建案例


5.按住ctrl可以按步长移动,edit->step setting可以更改步长

6.v工具，长按键盘的v键，长按以后就会自动吸附选定模型顶点

7.【bug处理】There are 2 audio listeners in the scene. 
Please ensure there is always exactly one audio listener in the scene.
是因为后来创建了一个camera，因为camera中自带一个组件Audio Listener。
所以有两个camera就有两个audio listener导致报错。
一个简单的解决方法就是删掉其中一个camera中的audio listener组件


二 :ui界面设计


8.hierarchy中新建UI中canvas，
  然后修改render mode的参数，改为第二个camera
  将main camera 拖入render camera
  修改摄像机与ui平面的距离：plane distance改为5

9.ui是浮在屏幕上的，并不属于游戏空间
  显然，text/button/toggle并不算是一个空间中的物体
  
10.text控件
  10.1）inspector中勾选 best fit
  10.2）font zise：字体大写
  10.3）alignment：对齐，支持多行文本
  10.4）best fit：根据rect自动调整字体大小
  10.5）font：字体，支持ttf和otf

11.image控件
  11.1）image type:填充类型
        simple:拉伸
        sliced:九宫格
        tiled:平铺
        filled:充满
  11.2）九宫格方式填充，适用于带边框的图片
        11.2.1）修改图片素材，sprite editor，定义九宫格
        11.2.2）添加image元素，选中图片素材
        11.2.3）将image type设为sliced
        11.2.4）改变image元素的矩形框大小，观察是否有畸形
        四个角比例时不变的，只会拉伸中间

12.button控件 
  12.1）transition设为color tint 表示普通的颜色按钮
  12.2）transition设为sprite swap 表示图片按钮

13.input field控件

14.事件处理
   14.1）添加"游戏主控"节点、挂载mygame.cs
         挂载脚本有一个login方法，希望在点登录的时候显示
        public void Login()
        {
            Debug.Log("logining....");
        }
         点击登录，在inspertor中找到on clik（）并点击加号
         然后将游戏主控拖入
         选中登录->login（）方法
   14.2）添加一个处理方法login（）
   14.3）在button组件下，添加onclick的事件处理
         在denglu代码文件中加入
         public InputField userfield;
         返回游戏主控，选择insopector，将hierarchy中用户名拖入userfield
         string user = userfield.text;
         Debug.Log(user+"logining....");
   14.4）自定义的按钮，挂脚本，实现IPoniterDownHandler接口
         public class OKButton : MonBehaviour,IPointDownHandler
         重写方法
         public void OnPointerDown(pointerEventDate eventData)
         {
             throw new system.NotImplementdException();
         }                        
                                 

15.ui布局
   15.1）rect transform的定位
         默认居中定位
         pos x/y.width/height
         改变game窗口大小，text与canvas中心的距离是不变的


16.新建场景：ctrl+n
 
17.加载新场景
    17.1）定义一个方法，挂载在新建的脚本文件中（gamemanger）
       public void OnStartGame(string scenceName)
       {
          //需要调用新场景的名字
           Application.LoadLevel(scenceName);

       }

       更新：
       SceneManager.LoadScene(scenceName);
       头文件：
       using UnityEngine.SceneManagement;
    17.2）在sencen1中canvas中startgame按钮中添加一个on click
    17.3）将gamemanger拖过去
    17.4）右边改为GameManger中自定义的OnStartGame
    17.5）参数改为下一个场景名称sence2
    17.6）file中buildsetting，将scence两个场景拖入scences in build中

18.密码输入，将text的inspector属性中的conetnt type改为password

19.一个显示结果的简单计算器
    19.1）先创建一个显示结果的文本框命名为result
    19.2）创建两个输入框，在text文本框下边，叫input1，input2
          并将content type改为integer number（只允许输入整数
    19.3）新建两个按钮，一个叫conclude，一个叫tanchu
    19.4）创建一个panel
    19.5）在panel中创建一个text，显示请输入
          创建一个inputfield
          创建两个按钮：ok，notok
          将panel隐藏（取消 勾选panel旁边tag上边的框框）
    19.6）新建一个代码文件，叫input，双击打开
          using System.Collections;
          using System.Collections.Generic;
          using UnityEngine;
          using UnityEngine.UI;
          using UnityEngine.EventSystems;

          public class input : MonoBehaviour
         {
          //申请变量
           public Text result;
           public InputField input1;
           public InputField input2;
           public InputField InutField;

           public void conclude()
           {
           //显示计算结果
           result.text=(int.Parse(input1.text) - int.Parse(input2.text)).ToString();

           }
         }
    19.7）将脚本放到计算的按钮上
    19.8）关联变量
    19.9）关联事件
          点击加号
          将自己拖入
          右边函数选计算
    19.10）显示弹出面板
           申请一个game object类型变量 叫panel
           public void tanchu()
           {
           panel.gameObject.SetActive(true);
           } 
           保存，然后在计算（conclude）中关联
           在tanchu按钮中添加点击事件（还在conclude上）
           input.tanchu






