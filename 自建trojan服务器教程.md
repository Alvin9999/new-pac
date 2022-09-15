**2022年9月15日更新。vultr更新了规则，开通服务器后必须手动在网站服务器后台关闭防火墙，不然无法用SSH工具去链接服务器，也就是默认的22端口是关闭的，关闭防火墙教程已更新。**

**如果无法查看图片，可以访问https://tr3.freeair888.club/自建trojan服务器教程/**

***

**整个教程分四步**：

第一步：购买VPS服务器

第二步：购买域名

第三步：一键搭建服务器

第四步：一键加速VPS服务器 （五合一的TCP网络加速脚本）


***

**第一步：购买VPS服务器**

VPS服务器需要选择国外的，首选国际知名的vultr，速度不错、稳定且性价比高，按小时计费，能够随时开通和删除服务器，新服务器即是新ip。

vultr注册地址：https://www.vultr.com/?ref=7048874 （vps最低2.5美元/月，vultr全球17个服务器位置可选，包括日本、韩国、新加坡、洛杉矶、德国、荷兰等。支持支付宝和paypal付款。） 

<a href="https://www.vultr.com/?ref=7048874"><img src="https://www.vultr.com/media/banners/banner_728x90.png" width="728" height="90"></a>

虽然是英文界面，但是现在的浏览器都有网页翻译功能，鼠标点击右键，选择网页翻译即可翻译成中文。

注册并邮件激活账号，充值后即可购买服务器。充值方式是支付宝或paypal，使用paypal有银行卡（包括信用卡）即可。paypal注册地址：https://www.paypal.com （paypal是国际知名的第三方支付服务商，注册一下账号，绑定银行卡即可购买国外商品）

***

2.5美元/月的服务器配置信息：单核   512M内存  10G SSD硬盘   带宽1G    500G流量/月   (**不推荐，仅提供ipv6 ip，不推荐**)

3.5美元/月的服务器配置信息：单核   512M内存  10G SSD硬盘   带宽1G    500G流量/月   (**推荐**)

5美元/月的服务器配置信息：  单核   1G内存    25G SSD硬盘   带宽1G    1000G流量/月  (**推荐**)
 
10美元/月的服务器配置信息： 单核   2G内存    55G SSD硬盘   带宽1G    2000G流量/月  

20美元/月的服务器配置信息： 2cpu   4G内存   80G SSD硬盘    带宽1G    3000G流量/月  

40美元/月的服务器配置信息： 4cpu   8G内存   160G SSD硬盘   带宽1G    4000G流量/月  

***

**注意：2.5美元套餐只提供ipv6 ip，一般的电脑用不了，所以建议选择3.5美元及以上的套餐。**

vultr实际上是折算成小时来计费的，比如服务器是5美元1个月，那么每小时收费为5/30/24=0.0069美元 会自动从账号中扣费，只要保证账号有钱即可。如果你部署的服务器实测后速度不理想，你可以把它删掉（destroy），重新换个地区的服务器来部署，方便且实用。因为新的服务器就是新的ip，所以当ip被墙时这个方法很有用。当ip被墙时，为了保证新开的服务器ip和原先的ip不一样，先开新服务器，开好后再删除旧服务器即可。在账号的Billing选项里可以看到账户余额。

**账号充值如图**：

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/pp100.png)

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/pp101.png)


**vultr改版了，最新开通服务器步骤如图**：

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new1.PNG)

选择“Cloud Compute”。

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new2.PNG)

选择“Regular Performance”。如果选择这个，在下面选择具体套餐的时候，最低是3.5美元/月（也要看服务器位置），流量是500GB/月；5美元是1T流量/月。

如果选择前面3个，在下面选择具体套餐的时候，最低是6美元/月，但6美元是2T流量/月。也就是，对流量需求较高的可以选择前面3个。

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new3.PNG)

选择服务器位置。不同的服务器位置速度会有所不同，有的服务器的最低价格会不同，一般纽约等位置的价格最低，有3.5美元/月的，可根据自己的需求来选择。

可以优先尝试洛杉矶服务器，亚洲服务器日本、韩国延迟较低，但用的人很多，国内速度不一定就会很好，当然其它服务器位置也可以尝试。

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new4.PNG)

**点击图中的系统名字，会弹出具体系统版本，推荐Debain10**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new5.PNG)

选择服务器套餐。根据自己的需求来选择，如果服务器位置定了，套餐不影响速度，影响流量和配置，一般用的人数少，选择低配置就够了。

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new6.PNG)

关闭自动备份，这个是收费的，可以关闭它。

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new7.PNG)

最后点击“Deploy Now”开始部署，等3~5分钟就差不多了。

**开通服务器时，当出现了ip，不要立马去ping或者用xshell去连接，vultr更新了规则，还需要手动关闭防火墙，方法在下方。完成购买后，找到系统的密码记下来，部署服务器时需要用到。vps系统的密码获取方法如下图：**

![](https://fastly.jsdelivr.net/gh/Alvin9999/crp_up/pac教程05.png)

![](https://fastly.jsdelivr.net/gh/Alvin9999/crp_up/pac教程06.png)


### vultr更新了规则，开通服务器后必须手动在网站服务器后台关闭防火墙，不然无法用SSH工具去链接服务器，也就是默认的22端口是关闭的。关闭防火墙方法：

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/vultr/vultr-firewall.png)

### 点击服务器的设置Settings——防火墙Firewall——选择No Firewall——点击更新Update FirewallGroup

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/vultr/vultr-firewall2.png)

### 之后等待120秒(2分钟)让设置生效，这样22端口就开放了。


**删掉服务器步骤如下图**：

删除服务器时，先开新的服务器后再删除旧服务器，这样可以保证新服务器的ip与旧ip不同。

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/ss/de4.PNG)

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/ss/de2.PNG)

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/ss/de5.png)

***


**第二步：购买域名**

有免费的域名，但为了稳定，建议选择付费的域名，因为免费的域名很可能会用不了多长时间。推荐用国外的域名服务商：[Namecheap](https://www.namecheap.com)，xyz、club后缀的域名1年1美元左右。

第一次购买域名，可以参考这个[域名购买教程](https://github.com/Alvin9999/new-pac/wiki/%E5%9F%9F%E5%90%8D%E8%B4%AD%E4%B9%B0%E6%95%99%E7%A8%8B) 。

***

**第三步：一键搭建VPS服务器**

购买服务器后，需要部署一下。因为你买的是虚拟东西，而且又远在国外，我们需要一个叫Xshell的软件来远程部署。Xshell windows版下载地址：

[国外云盘1下载](https://tr601.free4444.xyz/Xshell_setup_wm.exe)
[国外云盘2下载](https://tr201.free4444.xyz/Xshell_setup_wm.exe)

如果你是Mac苹果电脑操作系统，更简单，无需下载xshell，系统可以直接连接VPS。直接打开Terminal终端，输入：ssh root@43.45.43.21（将45.45.43.21换成你的IP），之后输入你的密码就可以登录了（输入密码的时候屏幕上不会有显示）

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/Mac.png)

如果不能用Mac自带的终端连接的话，直接网上搜“Mac连接SSH的软件”，有很多，然后通过软件来连接vps服务器就行，具体操作方式参考windows xshell。Mac成功连接vps后剩下的操作和windows一样。

***

部署教程：

下载windows xshell软件并安装后，打开软件

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/xshell11.png)

选择文件，新建

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/xshell12.png)

随便取个名字，然后把你的服务器ip填上

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/xshell13.png)

连接国外ip即服务器时，软件会先后提醒你输入用户名和密码，用户名默认都是root，密码是你购买的服务器系统的密码。

**如果xshell连不上服务器，没有弹出让你输入用户名和密码的输入框，表明你开到的ip是一个被墙的ip，遇到这种情况，重新开新的服务器，直到能用xshell连上为止，耐心点哦！如果同一个地区开了多台服务器还是不行的话，可以换其它地区。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/xshell14.png)

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/ss/xshell2.png)

连接成功后，会出现如上图所示，之后就可以复制粘贴代码部署了。

**一键安装trojan脚本代码（系统支持centos7+/debian9+/ubuntu16+）**：

***

bash -c "$(curl -fsSL https://raw.githubusercontent.com/atrandys/trojan/master/trojan_mult.sh)"

> 如果输入安装命令没反应，或者提示curl: command not found ，那是因为服务器系统没有自带curl命令，安装一下curl。

> CentOS系统安装curl命令：yum install -y curl   

> Debian/Ubuntu系统安装curl命令：apt-get install -y curl

***

复制上面整个代码到vps服务器中进行安装，安装过程中会提示输入域名。

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/trojan-new1.PNG)

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/trojan3.png)

安装过程会先提示输入域名，不要带http或https，只输入域名即可，例如domain.com或 a.domain.com ，之后提示输入密码时输入密码。

最终安装完成后，配置文件信息会自动展示在屏幕上，对于trojan账号信息，最重要的是域名和密码。以v2rayN客户端为例，填入方法如下图：

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/trojan-2.png)

打开v2rayN客户端——添加trojan服务器——填入账号信息，如上图，重要信息包括：域名、密码、传输层安全tls、SNI。

浏览器代理设置成socks5 127.0.0.1:1080。

谷歌浏览器chrome可配合switchyomega插件来使用，下载插件：[switchyomega](https://github.com/atrandys/trojan/releases/download/1.0.0/SwitchyOmega_Chromium.crx)

安装插件，打开chrome，打开扩展程序，将下载的插件拖动到扩展程序页面，添加到扩展。
![20181116000534](https://user-images.githubusercontent.com/12132898/70548725-0461d000-1bae-11ea-9d1e-4577e36ac46e.png)

完成添加，会跳转到switchyomega页面，点跳过教程，然后点击proxy，如图填写，最后点击应用选项。
![20181116001438](https://user-images.githubusercontent.com/12132898/70548727-04fa6680-1bae-11ea-99da-568af4fd6f5f.png)

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

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr1.jpg)

操作方法：先安装内核，重启vps让内核生效，再启动对应的加速即可。数字1的BBR/BBR魔改内核对应数字4、5、6的BBR加速、BBR魔改加速和暴力BBR魔改版加速。数字2的BBRplus内核对应数字7的BBRplus加速。数字3的锐速加速内核对应数字8的锐速加速。

以安装暴力BBR魔改版加速为例，我们先安装对应的内核，输入数字1

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr2.jpg)

内核安装完成后，输入y进行重启，重启才能让内核生效

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr3.jpg)

重启完成后，输入数字6来启动暴力BBR魔改版加速

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr4.jpg)

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr5.jpg)

输入./tcp.sh查看最终是否启动成功。

如果想换一个加速，输入数字9进行卸载加速，然后进行同样的操作，安装内核再安装对应内核的加速即可。

**注意：如果在安装内核环节出现这样一张图，注意选择NO**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr6.jpg)

***

**常见问题参考解决方法**：

1、Trojan客户端打开无法运行，提示缺少找不到vcruntime140.dll或找不到msvcp140.dll。

原因缺少运行库，点击[下载链接](https://www.microsoft.com/en-us/download/details.aspx?id=48145)中的两个软件，一个是32位一个是64位，请全部安装即可。

2、如果遇到vcruntime140_1的错误，下载下面的文件放到C:\windows\system32目录下即可

[点击下载140_1.dll](https://github.com/atrandys/trojan/raw/master/vcruntime140_1.dll)

3、trojan服务端怎么修改密码

trojan服务端配置文件路径如下，如需修改内容，修改以下文件即可。

/usr/src/trojan/server.conf

修改完成后，重启trojan服务端即可，同时客户端的密码也要同步修改哦。

systemctl restart trojan

4、关于申请证书没有成果的处理

可能的原因1：

一些原因导致使用nginx申请证书时出错，要么防火墙端口没开放，要么nginx未正常。建议用最纯净的系统安装。

可能的原因2:

出现这个问题最可能的原因之一是你的同一个域名多次申请证书，导致let’s encrypt官方的限制，同一域名每周最多5次申请。

![](https://www.atrandys.com/wp-content/uploads/2019/10/clipboard.png)

如果你的同一个域名申请了很多此证书，这个处理方法可能有用：更换二级域名，例如原来使用的域名是www.abc.com或abc.com或xyz.abc.com，那么现在你添加一个二级域名解析例如xxx.abc.com，安装时使用这个域名即可。

***


有问题可以发邮件至海外邮箱kebi2014@gmail.com
