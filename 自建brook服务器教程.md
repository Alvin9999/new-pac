**2024年1月1日更新，解决图片显示问题。**

***

**自建brook教程很简单，整个教程分三步**：

第一步：购买VPS服务器

第二步：一键部署VPS服务器

第三步：一键加速VPS服务器 （五合一的TCP网络加速脚本）

***

**【前言】**

Brook是一款新兴的代理软件，其版本横垮Windows、安卓、iOS、MacOS、Linux等多个系统平台，功能类似于我们经常使用的Shadowsocks/ShadowsocksR。Brook 的目标是简单易用、傻瓜化、速度快（新协议）。通过在服务器端安装Brook服务器端，同时在本地设备中使用Brook客户端，两者成功连接之后，可以为我们提供科学上网服务。如果你想在SS/SSR/V2ray之外，尝试一种新的代理软件，那么Brook是一个不错的选择！

***
**第一步：购买VPS服务器**

VPS服务器需要选择国外的，首选国际知名的vultr，速度不错、稳定且性价比高，按小时计费，能够随时开通和删除服务器，新服务器即是新ip。

vultr注册地址：https://www.vultr.com/?ref=7048874 （vps最低2.5美元/月，vultr全球25个服务器位置可选，包括洛杉矶、韩国、新加坡、日本、德国、荷兰等。支持支付宝和paypal付款。）  

<a href="https://www.vultr.com/?ref=7048874"><img src="https://www.vultr.com/media/banners/banner_728x90.png" width="728" height="90"></a>

虽然是英文界面，但是现在的浏览器都有网页翻译功能，鼠标点击右键，选择网页翻译即可翻译成中文。

注册并邮件激活账号，充值后即可购买服务器。充值方式是支付宝或paypal，使用paypal有银行卡（包括信用卡）即可。paypal注册地址：https://www.paypal.com （paypal是国际知名的第三方支付服务商，注册一下账号，绑定银行卡即可购买国外商品）

***


**注意：2.5美元套餐只提供ipv6 ip，一般的电脑用不了，所以建议选择3.5美元及以上的套餐。**

vultr实际上是折算成小时来计费的，比如服务器是5美元1个月，那么每小时收费为5/30/24=0.0069美元 会自动从账号中扣费，只要保证账号有钱即可。如果你部署的服务器实测后速度不理想，你可以把它删掉（destroy），重新换个地区的服务器来部署，方便且实用。因为新的服务器就是新的ip，所以当ip被墙时这个方法很有用。当ip被墙时，为了保证新开的服务器ip和原先的ip不一样，先开新服务器，开好后再删除旧服务器即可。在账号的Billing选项里可以看到账户余额。

**账号充值如图**：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/pp100.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/pp101.png)


**vultr改版了，最新开通服务器步骤如图**：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new1.PNG)

选择“Cloud Compute”。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new2.PNG)

选择“Regular Performance”。如果选择这个，在下面选择具体套餐的时候，最低是3.5美元/月（也要看服务器位置），流量是500GB/月；5美元是1T流量/月。

如果选择前面3个，在下面选择具体套餐的时候，最低是6美元/月，但6美元是2T流量/月。也就是，对流量需求较高的可以选择前面3个。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new3.PNG)

选择服务器位置。不同的服务器位置速度会有所不同，有的服务器的最低价格会不同，一般纽约等位置的价格最低，有3.5美元/月的，可根据自己的需求来选择。

电信用户推荐洛杉矶服务器；联通、移动用户推荐韩国、洛杉矶服务器。其它位置也可以尝试。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new4.PNG)

**点击图中的系统名字，会弹出具体系统版本，推荐Debain10**

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new5.PNG)

选择服务器套餐。根据自己的需求来选择，如果服务器位置定了，套餐不影响速度，影响流量和配置，一般用的人数少，选择低配置就够了。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new6.PNG)

关闭自动备份，这个是收费的，可以关闭它。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new7.PNG)

最后点击“Deploy Now”开始部署，等6~10分钟就差不多了。

**完成购买后，找到系统的密码记下来，部署服务器时需要用到。vps系统的密码获取方法如下图：**

![](https://cdn.jsdelivr.net/gh/Alvin9999/crp_up/pac教程05.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/Debian2.png)


**删掉服务器步骤如下图**：

删除服务器时，先开新的服务器后再删除旧服务器，这样可以保证新服务器的ip与旧ip不同。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/de4.PNG)

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/de2.PNG)

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/de5.png)


***

**第二步：部署VPS服务器**

购买服务器后，需要部署一下。因为你买的是虚拟东西，而且又远在国外，我们需要一个叫Xshell的软件来远程部署。Xshell windows版下载地址：

[国外云盘1下载](https://d2.freessr2.xyz/Xshell_setup_wm.exe)
[国外云盘2下载](https://d.dtku35.xyz/Xshell_setup_wm.exe)

如果你是Mac苹果电脑操作系统，更简单，无需下载xshell，系统可以直接连接VPS。直接打开Terminal终端，输入：ssh root@43.45.43.21（将45.45.43.21换成你的IP），之后输入你的密码就可以登录了（输入密码的时候屏幕上不会有显示）

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/Mac.png)

如果不能用Mac自带的终端连接的话，直接网上搜“Mac连接SSH的软件”，有很多，然后通过软件来连接vps服务器就行，具体操作方式参考windows xshell。Mac成功连接vps后剩下的操作和windows一样。

***

部署教程：

下载windows xshell软件并安装后，打开软件

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/xshell11.png)

选择文件，新建

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/xshell12.png)

随便取个名字，然后把你的服务器ip填上

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/xshell13.png)

连接国外ip即服务器时，软件会先后提醒你输入用户名和密码，用户名默认都是root，密码是你购买的服务器系统的密码。

**如果xshell连不上服务器，没有弹出让你输入用户名和密码的输入框，表明你开到的ip是一个被墙的ip，遇到这种情况，重新开新的服务器，直到能用xshell连上为止，耐心点哦！如果同一个地区开了多台服务器还是不行的话，可以换其它地区。**

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/xshell14.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/xshell2.png)

连接成功后，会出现如上图所示，之后就可以复制粘贴代码部署了。


**CentOS 6和7 / Debian 6+ / Ubuntu 14.04 + brook一键部署管理脚本**

**2020年9月1日，[brook](https://github.com/txthinking/brook/releases/tag/v20200909)进行了重大的更新，9月1日到最新的版本客户端和服务端必须是最新的。如果你使用的是9月1日之前的老客户端，脚本一还是能用，只是在安装的时候不能自动获取版本，需要手动输入版本号v20200801 如果你使用的是9月1日或最新的客户端版本，可以用脚本二来手动安装，几条命令就可以了。**

**方法一（老）：**

wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/brook.sh && chmod +x brook.sh  && bash brook.sh

> 如果提示 wget: command not found 的错误，这是你的系统精简的太干净了，wget都没有安装，所以需要安装wget。CentOS系统安装wget命令: yum install -y wget Debian/Ubuntu系统安装wget命令:apt-get install -y wget

**方法二（新）：**

curl -L https://github.com/txthinking/brook/releases/download/v20230401/brook_linux_amd64 -o /usr/bin/brook

chmod +x /usr/bin/brook

setsid brook server --listen :9999 --password hello

> 第一条命令是下载v20230401版本，第二条命令给brook赋予权限，最后一条命令的意思是启动brook并增加守护进程，这样当ssh窗口关闭时，brook仍然是运行的，端口设置为9999，密码设置为hello，端口和密码可以改成自己的

***

复制上面的**脚本一代码**到VPS服务器里，复制代码用鼠标右键的复制，然后在vps里面右键粘贴进去，因为ctrl+c和ctrl+v无效。接着按回车键，脚本会自动安装。以后只需要运行这个快捷命令就可以出现下图的界面进行设置，快捷管理命令为：bash brook.sh 或 ./brook.sh

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brook1.PNG)

出现上图表明脚本安装成功，脚本安装成功后就可以输入快捷管理命令bash brook.sh 或 ./brook.sh 如果输入了快捷管理命令后，出现“Permission denied”字样，如下图，接着需要输入命令：chmod +x brook.sh 然后再输入快捷管理命令即可。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brook2.PNG)

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brook3.PNG)

输入快捷管理命令后，出现上图，接着输入数字1来进行安装。会依次对**端口、密码、协议和版本号**进行选择。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brook4.PNG)

端口输入1-65535之间的数字。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brook5.PNG)

密码最好不要有特殊符号。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brook6.PNG)

协议选择新版协议，输入1。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brook7.PNG)

版本号输入v20200801

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brook8.PNG)

最终安装成功后，会出现下面的界面。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brook9.PNG)

此脚本是开机自动启动，部署一次即可。最后可以重启服务器确保部署生效（一般情况不重启也可以）。重启需要在命令栏里输入reboot ，输入命令后稍微等待一会服务器就会自动重启，一般重启过程需要2～5分钟，重启过程中Xshell会自动断开连接，等VPS重启好后才可以用Xshell软件进行连接。如果部署过程中卡在某个位置超过10分钟，可以用xshell软件断开，然后重新连接你的ip，再复制代码进行部署。

***

**第三步：一键加速VPS服务器**

五合一的TCP网络加速脚本，包括了BBR原版、BBR魔改版、暴力BBR魔改版、BBR plus（首选）、Lotsever(锐速)安装脚本。可用于KVMXen架构，不兼容OpenVZ（OVZ）。支持Centos 6+ / Debian 7+ / Ubuntu 14+，BBR魔改版不支持Debian 8。

***

wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh"

chmod +x tcp.sh

./tcp.sh


***

> 如果提示 wget: command not found 的错误，这是你的系统精简的太干净了，wget都没有安装，所以需要安装wget。CentOS系统安装wget命令: yum install -y wget Debian/Ubuntu系统安装wget命令:apt-get install -y wget

安装完成后，脚本管理命令为：./tcp.sh

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr1.jpg)

操作方法：先安装内核，重启vps让内核生效，再启动对应的加速即可。数字1的BBR/BBR魔改内核对应数字4、5、6的BBR加速、BBR魔改加速和暴力BBR魔改版加速。数字2的BBRplus内核对应数字7的BBRplus加速。数字3的锐速加速内核对应数字8的锐速加速。（如果服务器系统是Debain10或以上系统，可不用安装内核，直接输入数字4启动bbr原版加速。）

以安装暴力BBR魔改版加速为例，我们先安装对应的内核，输入数字1

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr2.jpg)

内核安装完成后，输入y进行重启，重启才能让内核生效

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr3.jpg)

重启完成后，输入数字6来启动暴力BBR魔改版加速

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr4.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr5.jpg)

输入./tcp.sh查看最终是否启动成功。

如果想换一个加速，输入数字9进行卸载加速，然后进行同样的操作，安装内核再安装对应内核的加速即可。

**注意：如果在安装内核环节出现这样一张图，注意选择NO**

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr6.jpg)

***

【**Brook windows客户端下载及使用方法**】

第一步：下载Brook Tools，**本软件是一个辅助软件（可视化UI操作），他无法独立使用，需要配合 Brook Windows命令行版客户端使用**。

Brook Tools v1.0.8 [下载地址1](https://d2.freessr2.xyz/BrookTools1.0.8.zip) [下载地址2](https://free.zhujicn2.net//BrookTools1.0.8.zip)

第二步：下载Brook Windows命令行版客户端，地址：https://github.com/txthinking/brook/releases ，如下图，windows32位系统选择第一个，64位系统选择第二个，下载后**重命名为**brook.exe

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brookwin1.png)

第三步：将下载好的Brook Tools压缩包解压出来，解压路径不要包含中文，将重命名好的Brook Windows命令行版客户端**放在同一个文件夹**。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brookwin2.png)

打开Brook Tools客户端，点击界面上的“浏览”后，打开同一文件夹的brook.exe ,之后点击“保存配置”、“启动”

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brookwin3.png)

Brook Tools客户端有2种代理方式，默认的是**http代理**，如果把前面的勾去掉，则变为**socks5代理**。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/brook/brookwin4.png)

浏览器代理相应设置为：如果是http代理，设置为HTTP 127.0.0.1 2080；如果是socks5代理，设置为socks5 127.0.0.1 2080；

谷歌浏览器可配合switchyomega插件来使用，下载插件：[switchyomega](https://github.com/atrandys/trojan/releases/download/1.0.0/SwitchyOmega_Chromium.crx)

安装插件，打开chrome，打开扩展程序，将下载的插件拖动到扩展程序页面，添加到扩展。
![20181116000534](https://user-images.githubusercontent.com/12132898/70548725-0461d000-1bae-11ea-9d1e-4577e36ac46e.png)

完成添加，会跳转到switchyomega页面，点跳过教程，然后点击proxy，如图填写，最后点击应用选项。

![](https://cdn.jsdelivr.net/gh/PAC/v2ray/bhttp.PNG)

***

**常见问题参考解决方法**：

1、账号无法使用，可能原因一：**客户端与服务端的设备系统时间相差过大。**

当vps服务器与本地设备系统时间相差过大，会导致客户端无法与服务端建立链接。请修改服务器时区，再手动修改服务器系统时间（注意也要校准自己本地设备时间）！

先修改vps的时区为中国上海时区：\cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime 

再手动修改vps系统时间命令的格式为（数字改为和自己电脑时间一致，误差30秒以内）：date -s "2020-2-02 19:14:00"   

修改后再输入date命令检查下。

2、账号无法使用，可能原因二：**客户端与服务端版本不一致**

因为 Brook 每次更新的内容可能变动较大，所以如果客户端与服务端版本不一致，那么很有可能会导致客户端链接服务端被拒绝。包括Brook Tools 里调用的 Windows 命令行版客户端，所以请尝试更新服务端或客户端为最新版本。比如教程演示中服务端的版本是v20190205，那么下载的命令行版客户端也最好是v20190205

3、账号无法使用，可能原因三：**Windows 防火墙、杀毒软件阻挡代理软件。**

如果以上问题都已排查，可以关闭 Windows 自带的防火墙、杀毒软件再尝试。

4、搭建的账号之前能用，突然不能用了，怎么解决？

如果ip不能ping通，xshell不能直接连接vps服务器，说明ip被墙了，需要开新服务器换ip。

如果ip能ping，xshell能直接连接vps服务器，说明ip没有被墙，多半是端口被封了，优先换端口。


***


有问题可以发邮件至海外邮箱rebeccalane27@gmail.com
