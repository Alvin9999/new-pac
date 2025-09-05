**2025年9月5日更新。**

***

**自建v2ray教程很简单，整个教程分三步**：

第一步：购买VPS服务器 

第二步：一键部署VPS服务器

第三步：一键加速VPS服务器 （五合一的TCP网络加速脚本）

***

**【前言】**

**v2ray的优势**：v2ray支持的传输方式有很多，包括：普通TCP、HTTP伪装、WebSocket流量、普通mKCP、mKCP伪装FaceTime通话、mKCP伪装BT下载流量、mKCP伪装微信视频流量，不同的传输方式其效果会不同，有可能会遇到意想不到的效果哦！当然国内不同的地区、不同的网络环境，效果也会不同，所以具体可以自己进行测试。现在v2ray客户端也很多了，有windows、MAC、linux和安卓版。

***

**第一步：购买VPS服务器**

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

点击图中的系统名字，会弹出具体系统版本，推荐Debian

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

***

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

**一键部署sing-box管理脚本（推荐Debian系统）**

安装依赖:

```bash
apt update && apt -y install curl wget nginx  tar socat jq git openssl uuid-runtime build-essential zlib1g-dev libssl-dev libevent-dev dnsutils cron
```

**安装依赖有点慢，耐心等待自动安装完成。Debian系统安装很快，Ubuntu系统安装要慢一点。**

安装脚本:

```bash
bash <(wget -qO- https://raw.githubusercontent.com/fscarmen/sing-box/main/sing-box.sh)
```

> 安装完成后，输入 sb 可进入管理页面。


***

**脚本演示**

复制上面安装命令代码到VPS服务器里，复制代码用鼠标右键的复制，然后在vps里面右键粘贴进去，因为ctrl+c和ctrl+v无效。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-v2ray1.png)

输入2，选择中文

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-v2ray2-2.png)

输入1，安装

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-v2ray3.png)

输入a，选择全部类型

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-v2ray4-2.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-v2ray5.png)

全部回车

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-v2ray6.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-v2ray7.png)

出现上面字样表示安装成功

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-v2ray8.png)

安装完成后，节点会有多种类型的输出形式，适合多个不同的客户端导入，从上往下包括v2rayN、ShadowRocket、 Clash Verge、NekoBox、Sing-box。如果是用v2ray客户端，鼠标一直往上面翻，找到v2rayN下面的所有节点，有鼠标右键全部复制下来，一键全部倒入到软件中。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-v2ray9.png)

目前有9个不同类型的节点，有6～7个节点可以用。

***

**如果选择的是CentOS系统，还需要关闭vps防火墙来开放端口，相关命令如下：**

**查看防火墙状态命令**：
```bash
firewall-cmd --state
```
**停止firewall命令**：
```bash
systemctl stop firewalld.service
```
**禁止firewall开机启动命令**：
```bash
systemctl disable firewalld.service
```

***


**第三步：一键加速VPS服务器**

五合一的TCP网络加速脚本，包括了BBR原版（首选）、BBR Plus、BBR魔改版、暴力BBR魔改版、LotServer(锐速)安装脚本。可用于KVMXen架构，不兼容OpenVZ（OVZ）。支持Centos 6+ / Debian 7+ / Ubuntu 14+，BBR魔改版不支持Debian 8。

👉 强烈推荐使用 BBR 原版加速：最稳定——谷歌官方维护，速度不错；最省心——Debian 9+ / Ubuntu 18.04+  系统无需更换内核；最安全——避免因魔改内核导致 VPS 无法启动。

⚠️ 其他版本（BBR Plus / 魔改 / 暴力魔改 / 锐速）需要更换或指定内核，风险较高，不推荐新手使用。

***

```bash
wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh"
chmod +x tcp.sh
./tcp.sh
```
***

> 如果提示 wget: command not found 的错误，这是你的系统精简的太干净了，wget都没有安装，所以需要安装wget。CentOS系统安装wget命令: yum install -y wget Debian/Ubuntu系统安装wget命令:apt-get install -y wget

安装完成后，脚本管理命令为：./tcp.sh

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-bbr-1.png)

如果服务器系统是 **Debian** 或 **Ubuntu**，可不用安装内核，直接输入 **数字 4** 启动 **BBR 原版加速**。  

如果服务器系统是 **CentOS**，先输入 **数字 1** 安装内核，然后 **重启服务器** 后，输入 **数字 4** 启动 **BBR 原版加速**。  

**BBR 原版**由谷歌官方开发，稳定且速度表现优秀，推荐使用。  

⚠️ **注意**：对于其他第三方内核，可能存在与系统不兼容的情况，安装后有概率导致 **VPS 无法正常启动**，需谨慎，因此 **不推荐**。 如果VPS 无法正常启动需要重装系统或者开新服务器。

以安装**BBR 原版加速**为例，输入加速脚本，选择数字4

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-bbr-1.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-bbr-2.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-bbr-3.png)

输入./tcp.sh查看最终是否启动成功。

如果想换一个加速，输入数字9进行卸载加速，然后进行操作。

**注意：如果在安装内核环节出现这样一张图，注意选择NO**

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/newbbr6.jpg)

***

【v2ray客户端下载及使用方法】

**客户端使用教程：[v2ray各平台图文使用教程](https://github.com/Alvin9999/new-pac/wiki/v2ray%E5%90%84%E5%B9%B3%E5%8F%B0%E5%9B%BE%E6%96%87%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)**

**软件代理设置**：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v2rayn001.jpg)

windows系统打开v2rayN软件，在软件的底部，选择“自动配置系统代理”，路由可选择“全局(Global)”。全局(Global)模式：所有网站通过节点服务器代理上网。

***


有问题可以发邮件至海外邮箱rebeccalane27@gmail.com
