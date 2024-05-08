## 背景
有用户想要离线版的NRSDK文档

## Dev log
一开始尝试将HTML文件导出为PDF，[ILovePDF](https://www.ilovepdf.com/zh-cn/html-to-pdf)导出得挺不错的，但是有一些长页面处理起来很吃力。
也找了一些代码的处理方式，可以看main.py，但是仍然很慢，效果不理想。

后来尝试使用直接在网页上右键保存为HTML的方式，意外发现效果很好，PDF看不了动图，离线HTML却可以。

![image](https://github.com/dengxian-xreal/HTML2PDF/assets/134575521/585cc5ef-650b-4651-bc29-75f3c9379d41)

而且网页原本的各种交互都还在。
但是全部网页在一个文件夹里，找起来很不方便。

![image](https://github.com/dengxian-xreal/HTML2PDF/assets/134575521/c16a670e-3f5e-4c11-bfce-118e04eb5e8e)

尝试处理这些HTML files：

首先是需要重命名：**rename.py**
其次是将导航栏中的跳转链接给替换了：**replace.py**

然后就大功告成啦。
