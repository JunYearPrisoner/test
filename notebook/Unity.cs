                                         Unity

1.scene          �����༭����
  game           ��Ϸ���д���
  hierarchy      �������� �б���
  project        ��Ŀ��Դ �б���
  inspector      ���Ա༭ �б���


2.File         �ļ��˵�
  Edit         �༭�˵�
  Assets       ��Դ�˵�
  GameObject   ����˵�
  Component    ����˵�
  Window       ���ڲ˵�
  Help         �����˵�

 
3.scene�����Ϸ����ĸ���������ͬ��qwer�����л�


4.hierarchy�볡���

   4.1���������
      4.1.1)camera ��ʾ�û�����������Ұ�����·�С�������game����Ұ����ͬ��
      4.1.2��inspector��death��ʾcamera�����ȼ�
            deathԽ�����ȼ�Խ��
   4.2���ƹ����
   4.3���������
   4.4���������
   4.5���㼶��ϵ������
   4.6�����������


5.��סctrl���԰������ƶ�,edit->step setting���Ը��Ĳ���

6.v���ߣ��������̵�v���������Ժ�ͻ��Զ�����ѡ��ģ�Ͷ���

7.��bug����There are 2 audio listeners in the scene. 
Please ensure there is always exactly one audio listener in the scene.
����Ϊ����������һ��camera����Ϊcamera���Դ�һ�����Audio Listener��
����������camera��������audio listener���±���
һ���򵥵Ľ����������ɾ������һ��camera�е�audio listener���


�� :ui�������


8.hierarchy���½�UI��canvas��
  Ȼ���޸�render mode�Ĳ�������Ϊ�ڶ���camera
  ��main camera ����render camera
  �޸��������uiƽ��ľ��룺plane distance��Ϊ5

9.ui�Ǹ�����Ļ�ϵģ�����������Ϸ�ռ�
  ��Ȼ��text/button/toggle��������һ���ռ��е�����
  
10.text�ؼ�
  10.1��inspector�й�ѡ best fit
  10.2��font zise�������д
  10.3��alignment�����룬֧�ֶ����ı�
  10.4��best fit������rect�Զ����������С
  10.5��font�����壬֧��ttf��otf

11.image�ؼ�
  11.1��image type:�������
        simple:����
        sliced:�Ź���
        tiled:ƽ��
        filled:����
  11.2���Ź���ʽ��䣬�����ڴ��߿��ͼƬ
        11.2.1���޸�ͼƬ�زģ�sprite editor������Ź���
        11.2.2�����imageԪ�أ�ѡ��ͼƬ�ز�
        11.2.3����image type��Ϊsliced
        11.2.4���ı�imageԪ�صľ��ο��С���۲��Ƿ��л���
        �ĸ��Ǳ���ʱ����ģ�ֻ�������м�

12.button�ؼ� 
  12.1��transition��Ϊcolor tint ��ʾ��ͨ����ɫ��ť
  12.2��transition��Ϊsprite swap ��ʾͼƬ��ť

13.input field�ؼ�

14.�¼�����
   14.1�����"��Ϸ����"�ڵ㡢����mygame.cs
         ���ؽű���һ��login������ϣ���ڵ��¼��ʱ����ʾ
        public void Login()
        {
            Debug.Log("logining....");
        }
         �����¼����inspertor���ҵ�on clik����������Ӻ�
         Ȼ����Ϸ��������
         ѡ�е�¼->login��������
   14.2�����һ��������login����
   14.3����button����£����onclick���¼�����
         ��denglu�����ļ��м���
         public InputField userfield;
         ������Ϸ���أ�ѡ��insopector����hierarchy���û�������userfield
         string user = userfield.text;
         Debug.Log(user+"logining....");
   14.4���Զ���İ�ť���ҽű���ʵ��IPoniterDownHandler�ӿ�
         public class OKButton : MonBehaviour,IPointDownHandler
         ��д����
         public void OnPointerDown(pointerEventDate eventData)
         {
             throw new system.NotImplementdException();
         }                        
                                 

15.ui����
   15.1��rect transform�Ķ�λ
         Ĭ�Ͼ��ж�λ
         pos x/y.width/height
         �ı�game���ڴ�С��text��canvas���ĵľ����ǲ����


16.�½�������ctrl+n
 
17.�����³���
    17.1������һ���������������½��Ľű��ļ��У�gamemanger��
       public void OnStartGame(string scenceName)
       {
          //��Ҫ�����³���������
           Application.LoadLevel(scenceName);

       }

       ���£�
       SceneManager.LoadScene(scenceName);
       ͷ�ļ���
       using UnityEngine.SceneManagement;
    17.2����sencen1��canvas��startgame��ť�����һ��on click
    17.3����gamemanger�Ϲ�ȥ
    17.4���ұ߸�ΪGameManger���Զ����OnStartGame
    17.5��������Ϊ��һ����������sence2
    17.6��file��buildsetting����scence������������scences in build��

18.�������룬��text��inspector�����е�conetnt type��Ϊpassword

19.һ����ʾ����ļ򵥼�����
    19.1���ȴ���һ����ʾ������ı�������Ϊresult
    19.2�����������������text�ı����±ߣ���input1��input2
          ����content type��Ϊinteger number��ֻ������������
    19.3���½�������ť��һ����conclude��һ����tanchu
    19.4������һ��panel
    19.5����panel�д���һ��text����ʾ������
          ����һ��inputfield
          ����������ť��ok��notok
          ��panel���أ�ȡ�� ��ѡpanel�Ա�tag�ϱߵĿ��
    19.6���½�һ�������ļ�����input��˫����
          using System.Collections;
          using System.Collections.Generic;
          using UnityEngine;
          using UnityEngine.UI;
          using UnityEngine.EventSystems;

          public class input : MonoBehaviour
         {
          //�������
           public Text result;
           public InputField input1;
           public InputField input2;
           public InputField InutField;

           public void conclude()
           {
           //��ʾ������
           result.text=(int.Parse(input1.text) - int.Parse(input2.text)).ToString();

           }
         }
    19.7�����ű��ŵ�����İ�ť��
    19.8����������
    19.9�������¼�
          ����Ӻ�
          ���Լ�����
          �ұߺ���ѡ����
    19.10����ʾ�������
           ����һ��game object���ͱ��� ��panel
           public void tanchu()
           {
           panel.gameObject.SetActive(true);
           } 
           ���棬Ȼ���ڼ��㣨conclude���й���
           ��tanchu��ť����ӵ���¼�������conclude�ϣ�
           input.tanchu






