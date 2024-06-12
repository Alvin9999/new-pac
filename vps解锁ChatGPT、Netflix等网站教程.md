**2024年6月12日发布。**

***

如果你的vps搭建翻墙工具后不能访问[ChatGPT](https://chatgpt.com)、[Netflix](https://www.netflix.com)等网站，出现以下界面：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/chatgpt1.png)

解锁后可以不用登录账号访问ChatGPT。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/netflix1.png)

Netflix无法访问页面。


一般来说，需要原生ip才能正常访问这些受限制的网站，但原生ip的vps比较难找，且比较贵，因此我们可以借助Cloud­flare WARP来实现原生ip的功能。如果不想搭建vps，那么也可以考虑这个原生ip [V2free机场](https://github.com/Alvin9999/new-pac/wiki/V2free%E6%9C%BA%E5%9C%BA)。

***

通过脚本搭建好后，预览图如下

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/chatgpt6.jpg)

此时以上网站都可以正常访问了。

***

### 第一步：购买服务器

VPS服务器需要选择国外的，首选国际知名的vultr，速度不错、稳定且性价比高，按小时计费，能够随时开通和删除服务器，新服务器即是新ip。

vultr注册地址：https://www.vultr.com/?ref=7048874 （vps最低2.5美元/月，vultr全球32个服务器位置可选，包括洛杉矶、韩国、新加坡、日本、德国、荷兰等。支持支付宝和paypal付款。） 

<a href="https://www.vultr.com/?ref=7048874"><img src="https://www.vultr.com/media/banners/banner_728x90.png" width="728" height="90"></a>

虽然是英文界面，但是现在的浏览器都有网页翻译功能，鼠标点击右键，选择网页翻译即可翻译成中文。

注册并邮件激活账号，充值后即可购买服务器。充值方式是支付宝或paypal，使用paypal有银行卡（包括信用卡）即可。paypal注册地址：https://www.paypal.com （paypal是国际知名的第三方支付服务商，注册一下账号，绑定银行卡即可购买国外商品）

***

**注意：2.5美元套餐只提供ipv6 ip，一般的电脑用不了，所以建议选择3.5美元及以上的套餐。**

vultr实际上是折算成小时来计费的，比如服务器是5美元1个月，那么每小时收费为5/30/24=0.0069美元 会自动从账号中扣费，只要保证账号有钱即可。如果你部署的服务器实测后速度不理想，你可以把它删掉（destroy），重新换个地区的服务器来部署，方便且实用。因为新的服务器就是新的ip，所以当ip被墙时这个方法很有用。当ip被墙时，为了保证新开的服务器ip和原先的ip不一样，先开新服务器，开好后再删除旧服务器即可。在账号的Account——Make a payment选项里可以看到账户余额。

**账号充值如图**：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v0.jpg)

依次点击Account——Make a payment——Alipay(支付宝)

**vultr改版了，最新开通服务器步骤如图**：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v1.jpg)

点击网页右上角的Deploy图标

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v2.jpg)

在下拉菜单中，点击Deploy New Server

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v3.jpg)

服务器类型选择Cloud Compute-Shared CPU

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v4.jpg)

选择服务器位置。不同的服务器位置速度会有所不同，有的服务器的最低价格会不同，一般纽约等位置的价格最低，有3.5美元/月的，可根据自己的需求来选择。推荐洛杉矶服务器，延迟较低且比较稳定。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v5.jpg)

点击图中的系统名字，会弹出具体系统版本，推荐Debain10、Debain11 或者 CentOS7 （不要选默认的CentOS8，脚本不支持CentOS8）

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v6.jpg)

选择服务器套餐。根据自己的需求来选择，如果服务器位置定了，套餐不影响速度，影响流量和配置，一般用的人数少，选择低配置就够了。便宜的套餐，点击Regular Cloud Compute，选择第一个套餐，提示升级选择No Thanks。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v7.jpg)

关闭自动备份Auto Backups，这个是收费的。点击它，在右侧的I understand the risk前面选择勾，然后点击Disable Auto Backups即可关闭自动备份。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v8.jpg)

最后点击“Deploy Now”开始部署，等6~10分钟就差不多了。

**完成购买后，找到系统的密码记下来，部署服务器时需要用到。vps系统的密码获取方法如下图：**

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v9.jpg)

点击Products——Compute就可以看到购买的服务器列表

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v10.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v11.jpg)

在服务器的最右边，点击三个点，再点击Server Details就可以看到该服务器的详细信息。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v12.jpg)

服务器ip和系统密码可以看到并能复制。

**删掉服务器步骤如下图**：

删除服务器时，先开新的服务器后再删除旧服务器，这样可以保证新服务器的ip与旧ip不同。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/de2.PNG)

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/de5.png)

**第二步：部署VPS服务器**

购买服务器后，需要部署一下。因为你买的是虚拟东西，而且又远在国外，我们需要一个叫Xshell的软件来远程部署。Xshell windows版下载地址：

xshell5:

[国外云盘1下载](https://d2.freessr2.xyz/Xshell_setup_wm.exe)
[国外云盘2下载](https://d.dtku35.xyz/Xshell_setup_wm.exe)

**注意：如果使用xshell5的过程中提示“找不到匹配的host key算法”，可以下载更高的版本来解决，比如xshell7，可在xshell中文官方网站下载**：https://www.xshell.com/zh/free-for-home-school

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

***

本方法默认服务器已经安装了ss、v2ray、hysteria等工具。如果服务器没有安装翻墙工具，可以选择以下方法：

[自建ss/ssr服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAss%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 
[自建v2ray服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAv2ray%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 
[自建hysteria服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAhysteria%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B)
 
[一键搭建多个协议节点教程](https://github.com/Alvin9999/new-pac/wiki/%E4%B8%80%E9%94%AE%E6%90%AD%E5%BB%BA%E5%A4%9A%E4%B8%AA%E5%8D%8F%E8%AE%AE%E8%8A%82%E7%82%B9%E6%95%99%E7%A8%8B)  

[自建brook服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAbrook%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 
[自建trojan服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAtrojan%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 
[自建WireGuard VPN服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAWireGuard-VPN%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 

***

**Cloud­flare WARP 一键安装脚本**

```bash
bash <(wget -qO- https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh 2> /dev/null)
```

或者

```bash
bash <(curl -Ls https://gitlab.com/rwkgyg/CFwarp/raw/main/CFwarp.sh)
```

千万要注意：如出现IP丢失、VPS运行卡顿、脚本运行下载失败、无法进入脚本界面等现象，请用以下命令终止warp，再重启或者重装warp

1、终止warp-go： kill -15 $(pgrep warp-go)

2、终止wgcf： systemctl stop wg-quick@wgcf

***

演示操作：

复制上面的Cloud­flare WARP 一键安装脚本代码到VPS服务器里，复制代码用鼠标右键的复制，然后在vps里面右键粘贴进去，因为ctrl+c和ctrl+v无效。接着按回车键，脚本会自动安装。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/chatgpt2.jpg)

首次安装后，脚本会自动检测ChatGPT、Netflix解锁情况。从图片可以看出这台vultr vps都未解锁ChatGPT、Netflix。

输入数字2，安装wgcf。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/chatgpt3.jpg)

输入数字1，选择方案一。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/chatgpt4.jpg)

如果你的vps只有ipv4，那么选择数字1（单栈ipv4）；如果你的vps只有ipv6，那么选择数字2（单栈ipv6）；如果你的vps同时有ipv4和ipv6，那么选择数字3（双栈ipv4+ipv6）。

演示vultr vps为双栈ipv4+ipv6，所有选择数字3。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/chatgpt6.jpg)

出现这个界面表示安装成功了，从图片可以看出这台vultr vps已经成功解锁ChatGPT、Netflix。

测试：

打开ChatGPT官网：https://chatgpt.com

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/chatgpt7.jpg)

无需登录ChatGPT即可聊天。

打开Netflix官网：https://www.netflix.com

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/netflix3.png)

**注意**：通过此方法检测出来的落地ip为Cloud­flare WARP的ip，相当于服务器ip伪装成了Cloud­flare WARP的ip。但你的ss、v2ray等搭建好的账号的ip还是要填写vps的ip。另外，ssr账号用此方法测试不成功，ss、v2ray、hysteria账号测试可行。

ip检测网址：https://allinfa.com/tool/ip2/ip.php

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ipcheck1.png)

***

有问题可以发邮件至海外邮箱rebeccalane27@gmail.com
