**2025年9月15日更新。**

***

如果你的vps搭建翻墙工具后不能访问[Netflix](https://www.netflix.com)、[ChatGPT](https://chatgpt.com)等网站，比如出现Netflix无法访问页面：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/netflix1.png)

（如果访问YouTube出现需要登录账号才能观看视频，也可以用此方法来解决）

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

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025vultr-1.png)

服务器类型选择Shared CPU，选择服务器位置。不同的服务器位置速度会有所不同。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025vultr-2.png)

选择服务器套餐。有的服务器的最低价格会不同，一般纽约等位置的价格最低，有3.5美元/月的，可根据自己的需求来选择。推荐洛杉矶服务器，延迟较低且比较稳定。注意：2.5美元/月的套餐只提供ipv6，没有ipv4。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025vultr-3.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025vultr-4.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025vultr-5.png)

关闭自动备份Auto Backups，这个是收费的，每月1美元。点击它就可以省1美元，在右侧的I understand the risk前面选择勾，然后点击Disable Auto Backups即可关闭自动备份。接下来进行下一步，点击“Configure”

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025vultr-6.png)

点击图中的系统名字，会弹出具体系统版本，推荐Debian 11

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025vultr-7.png)

选择ipv4，不要选择ipv6，当同时选择ipv4和ipv6时，ipv4会被禁用。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025vultr-8.png)

最后点击“Deploy”开始部署，等3～5分钟就差不多了。

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

[国外云盘1下载](https://download.574981.xyz/Xshell_setup_wm.exe)
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

一键安装sing-box脚本，开箱即用 18 个节点（直连 9 + WARP 9），对于解锁网站需求，使用9个WARP节点。含端口一键切换、BBR 加速、分享链接导出等。支持系统：Debian 11+ / Ubuntu 20.04+ / CentOS Stream 9+ / Rocky 9+ / AlmaLinux 9+ / Fedora 38+ / Arch(rolling) / openSUSE Leap 15.4+，已在[Vultr](https://www.vultr.com/?ref=7048874) 上测试通过。脚本地址：[Alvin9999/Sing-Box-Plus](https://github.com/Alvin9999/Sing-Box-Plus)

```bash
wget -O sing-box-plus.sh https://raw.githubusercontent.com/Alvin9999/Sing-Box-Plus/main/sing-box-plus.sh && chmod +x sing-box-plus.sh && bash sing-box-plus.sh
```
> 安装完成后，输入 bash sing-box-plus.sh 可进入管理页面。

> 如果安装过其它 sing-box 脚本，请先卸载。

***

**脚本演示**

复制上面安装命令代码到VPS服务器里，复制代码用鼠标右键的复制，然后在vps里面右键粘贴进去，因为ctrl+c和ctrl+v无效。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-sing-box-1.png)

复制脚本后，按回车键。脚本会先安装相关依赖。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-sing-box-0.png)

出现管理界面后，输入数字 1 安装脚本。脚本全自动安装。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-sing-box-3.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-sing-box-4.png)

## ✨ 默认部署内容（18 个节点）

**直连 9：**

* VLESS Reality（Vision 流）
* VLESS gRPC Reality
* Trojan Reality
* VMess WS
* Hysteria2（直连证书）
* Hysteria2 + OBFS(salamander)
* Shadowsocks 2022（2022-blake3-aes-256-gcm）
* Shadowsocks（aes-256-gcm）
* TUIC v5（ALPN h3，自签证书）

​**WARP 9：**（同上 9 种，出站经 Cloudflare WARP）

> WARP 出站更利于流媒体解锁与回程质量。

用鼠标复制所有节点链接一键导入到软件中。以v2ray为例，导入后界面：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-sing-box-5.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-sing-box-6.png)

脚本还有其它功能：查看分享链接、一键更换所有端口 、一键开启 BBR。可以输入数字 5 来启动 BBR 加速，这样就不用单独部署 BBR 加速脚本。


***

有问题可以发邮件至海外邮箱rebeccalane27@gmail.com
