                    git ��GitHub

1.git�����в���
   1.1���ؿ��ʼ��
      1.1.1���git init
         11750@DESKTOP-URTIHVE MINGW64 /d/Git/CeShi
         $ git init
         Initialized empty Git repository in D:/Git/CeShi/.git/

         11750@DESKTOP-URTIHVE MINGW64 /d/Git/CeShi (master)
         $ ls -lA
         total 4
         drwxr-xr-x 1 11750 197609 0  6�� 27 14:04 #.git

         11750@DESKTOP-URTIHVE MINGW64 /d/Git/CeShi (master)
         $ ll .git/
         total 7
        -rw-r--r-- 1 11750 197609 130  6�� 27 14:04 config
        -rw-r--r-- 1 11750 197609  73  6�� 27 14:04 description
        -rw-r--r-- 1 11750 197609  23  6�� 27 14:04 HEAD
        -drwxr-xr-x 1 11750 197609   0  6�� 27 14:04 #hooks
        -drwxr-xr-x 1 11750 197609   0  6�� 27 14:04 #info
        -drwxr-xr-x 1 11750 197609   0  6�� 27 14:04 #objects
        -drwxr-xr-x 1 11750 197609   0  6�� 27 14:04 #refs
        #(ע�������#��#���ڵ��е�-����Ϊ�˽����)

      1.1.2 init ��ʼ������½�һ������Ŀ¼.git����������һЩ�����ļ�
      1.1.3 .gitĿ¼�д�ŵ��Ǳ��ؿ���ص���Ŀ¼���ļ�����Ҫɾ����Ҳ��Ҫ�����޸�

2.����ǩ��
   2.1��ʽ
      �û�����tzz
      Email��ַ��goodMorning@AKtgw.com
      ���ã����ֲ�ͬ������Ա�����
   
   2.2����
      ����Ŀ����/�ֿ⼶�𣺽��ڵ�ǰ��Ŀ��Ч
      ��ϵͳ�û����𣺵�¼��ǰ����ϵͳ���û���Χ
      ���ȼ�����������õĻ������վͽ�ԭ����Ч����ʹ����Ŀ���𲻻�ʹ��ϵͳ�û�
      !:���ұ�����һ��������û���ǲ������

   2.3 git config��������Ŀ����
         ��git congit user.name tzz
         ��git congit user.email goodMorning@AKtgw.com
       git config --global ������ϵͳ�û�����
         ��git config --global user.name tzz_glb 
         ��git config --global user.email goodMorning_glb@AKtgw.com

   2.4��Щ�����õ�.git/condigĿ¼�£�ʹ�� cat .git/config�鿴

3.�ύ
   3.1�ύ��git add �ļ���.�ļ�����
       ��������ǰ��һ����
       ��ͨ����Ŀͻ����������޸Ļ������ã�����
          ��git config --global core.autocrlf false
          ��git config --global core.safecrlf true
          https://blog.csdn.net/qq_42672770/article/details/86557593

       ��git config --global core.editor gvim
       �����ñ༭��λvim
       
   3.2�����ύ��git rm --cached �ļ���.�ļ�����  
   3.3���ݴ����ύ�����ؿ�
      git commit �ļ���.�ļ�����
      ��ʱ����git status�鿴����ʾ
        on branch master
        nothing to commit,working tree clean

      3.3.2 ����ʹ��git commit -m "�޸�����" �ļ���.�ļ�����
        ������༭�������ύ
        
      3.3.3���ύֻ����һ��     

4.��������
   ��������д����
   �ݴ�������ʱ�洢
   ���ؿ⣺��ʱ�汾
   4.1״̬�鿴����
      git status
      �鿴���������ݴ���״̬

   4.2��Ӳ���
      git add
      ����������"�޸�/�½�"��ӵ��ݴ���

   4.3�ύ����
      git commit -m "�޸�����" 
      ���ݴ����������ύ�����ؿ�

   4.4�汾��¼
      git log
      �����¼����һ���Ų��£����ո��������һҳ�л���b����
      ps����Linux��less����һ��
      ��q�˳���־
      git log --pretty=oneline #��һ����ʾÿ����־����ϣֵ��ʾȫ��
      git log --online #��ϣֵ��ʾ����
      git reflog(��ʾ����)

   4.5��������ֵ�ĺ���  
      git reset --hard ��ϣֵ(��reflog��ʾ����)
      ��������ֵ��ǰ��
      git reset --hard ��ϣֵ(��reflog��ʾ����)

   4.6����^��~�ĺ���
      git reset --hard HEAD^(���뵽��һ���汾)
      �������ŵĸ���ȥ���� һ������һ�� ������������
      tail����ʾ�ı������n�У��磺tail -n 3 �ļ���.�ļ���ʽ
      git log --oneline ֻ��ʾ��ߵİ汾������ʾǰ��İ汾
      ���߿�����~3��ʾ�������� д����������ͬ

5.git�ĵ��Ĳ鿴
   git help ��������

6.reset���������ĶԱ�   
   6.1 soft �����ڱ��ؿ��ƶ�headָ��
       �����޸ı����ļ�
   6.2  mixed 
       ���ڱ��ؿ��ƶ�headָ��
       �������ݴ���
        �����޸ı����ļ�
   6.3 ���ڱ��ؿ��ƶ�headָ��
       �������ݴ���
       �����ù���Ҳ

7.�ļ���ɾ��
   7.1ɾ��
      rm �ļ���.�ļ�����
      �����add�˻�
      ʹ��git status�鿴�����и����ֵ���ʾ
      �ٴ�ʹ��git add���ͻ��¼ɾ��
      ʹ��git commit�ύ ����ʷ��¼�оͻ����
      �Ϳ���ʹ��reset�ص�δ��ɾ����ʱ��
     
   7.2ɾ�����һ�
      ǰ�᣺ɾ��ǰ���ļ�����ʱ��״̬�ύ���˱��ؿ�
      ������git reset --hard[ָ��λ��]
            ָ��λ�ã���ʷ��¼����λ��
              �����ύ�����ؿ⣺ָ��λ��ָ����ʷ��¼
              ����δ�ύ�����ؿ⣺ָ��λ��ʹ��HEAD

8.�ļ��ıȽ�
   ���޸���һ���ļ��󣬿���ʹ��diff������в鿴�޸�ǰ��ıȽ�
   git diff �ļ���.�ļ�����
   �������add��֮����diff
   �Ͳ�������Ϣ��
   ���������HEAD �ͻ�����
   git diff HEAD �ļ���.�ļ�����

9.��֧����
   9.1 ��֧���ܣ�
       �·�֧��ϰ����feature_�������Ǵ����ɸ��ƹ����ģ�Ҳ����ʼʱ�·�֧������������ͬ
       ������֧�ڿ������������໥������
       ��֧�����ɣ�master��û���κ�Ӱ��
       ��֧Ҳ���Ժϲ�Ϊ���ɣ������ɶ����Ǵ�汾����
       ��������bug��һ�㴴��hot_fix��֧ȥ�޸��ٺϲ���һ�㲻ͣ����������������
   
   9.2 ��֧�鿴
       git branch -v

   9.3 ��֧����
       git branch ��֧��

   9.4 ��֧�л�
       git checkout ��֧��

   9.5 �ϲ���֧
       �����ڽ��ܺϲ����Ǹ���֧�£�����֧��
       Ȼ��ʹ��git merge ��֧����hot_fix��֧��

   9.6 ��֧��ͻ
       �����ֳ�ͻ���ֶ��޸�
       Ȼ������add����commit��commitʱ����Ҫ���ļ���

10.�ύ
   10.1 �鿴��ַ����
       git remote -v

   10.2 ����ַȡ����
       git remote add ���� ��ַ

   10.3 ����
       git push ���� ��֧��
       �ӱ��ؿ��ϴ�Զ�̿�

   10.4 ץȡ
       git fetch ���� ��֧��
       ��Զ�̿��ϴ����ؿ⣬���ǲ�����ı��ؿ��ļ�
       git checkout origin/main ���뵽����鿴
       Ȼ���� git merge origin/main(����/��֧��)��Զ�̿Ȿ�ؿ�ϲ�
       
   10.5 �ύ��ͻ
       ������ؿ�����°��ύʱ���ύʧ�ܣ�
       ��ʱpullһ�£�Ȼ����ֶ��޸ĳ�ͻ�ļ�����add����commit����push
       �ύ���ɲ����ļ���

       ���⣺pull=fetch+merge
