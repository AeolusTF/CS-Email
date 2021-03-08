# CS-Email

cobaltstrike上线邮箱提醒。

Github传送门：https://github.com/AeolusTF/CS-Email.git

## ABOUT：

首先，打开QQ邮箱，点击设置。

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/0.png)

点击账户

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/1.png)

需要打开SMTP服务

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/2.png)

发送短信验证开启

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/3.png)

之后会得到一个授权码，得到授权码保存下来！

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/4.png)

之后打开脚本，填入邮箱和授权码

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/5.png)

打开vps，把脚本放在cs目录下

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/6.png)

进入，log文件夹

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/7.png)

查看当前路径（pwd）

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/8.png)

创建后台任务，screen -S csjk

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/9.png)

运行脚本文件，并且输入你的log文件夹路径。

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/10.png)

脚本运行成功，Ctrl+A+D隐藏后台任务

screen -r 查看任务，cs邮箱提醒脚本是运行状态

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/11.png)

这时候就可以打开我们的cobaltstrike了！

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/12.png)

点击文件（我这边是用虚拟机进行调试的）

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/13.png)

邮件发过来了

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/14.png)

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/15.png)

![](https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/16.png)

Blog：https://aeolustf.github.io/2021/03/08/cobaltstrike%E9%82%AE%E7%AE%B1%E6%8F%90%E9%86%92/
