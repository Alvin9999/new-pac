**2024年8月8日更新。**

***

Hysteria 是一个功能丰富的，专为恶劣网络环境进行优化的网络工具（双边加速），比如卫星网络、拥挤的公共 Wi-Fi、在中国连接国外服务器等。 基于修改版的 QUIC 协议。由go编写的非常优秀的“轻量”代理程序，它很好的解决了在搭建科学上网服务器时的痛点——线路一般、高峰时期慢。虽然是走的udp但是提供obfs，暂时不会被运营商针对性的QoS(不开obfs也不会被QoS)。下图为原开发项目提供的不同协议的速度对比：

![](https://cdn.jsdelivr.net/gh/HyNetwork/hysteria/docs/bench/bench.png)

**自建hysteria教程很简单，整个教程分三步**：

第一步：购买VPS服务器

第二步：一键部署VPS服务器

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

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v3.jpg)

服务器类型选择Cloud Compute-Shared CPU

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v4.jpg)

选择服务器位置。不同的服务器位置速度会有所不同，有的服务器的最低价格会不同，一般纽约等位置的价格最低，有3.5美元/月的，可根据自己的需求来选择。推荐洛杉矶服务器，延迟较低且比较稳定。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v5.jpg)

点击图中的系统名字，会弹出具体系统版本，推荐Debain10、Debain11

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


***

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

注意：以下是安装hysteria 1脚本，教程的末尾是安装hysteria 2脚本。图文教程是安装hysteria 1。hysteria 1和2不兼容，安装hysteria 1后请使用hysteria 1相关的客户端。

***


**hysteria 1一键部署管理脚本：**

```bash
bash <(curl -fsSL https://git.io/hysteria.sh)
```

***

> 如果输入安装命令后提示curl: command not found，那是因为服务器系统没有自带curl命令，安装一下curl。

> CentOS系统安装curl命令：yum install -y curl

> Debian/Ubuntu系统安装curl命令：apt-get install -y curl

> 安装完成后，输入hihy可进入管理页面。脚本来自[emptysuns/Hi_Hysteria](https://github.com/emptysuns/Hi_Hysteria)。

***

复制上面的**脚本代码**到VPS服务器里，复制代码用鼠标右键的复制，然后在vps里面右键粘贴进去，因为ctrl+c和ctrl+v无效。接着按回车键，脚本会自动安装，以后只需要运行这个快捷命令就可以出现下图的界面进行设置，快捷管理命令为：hihy

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/hy1.png)

如上图出现管理界面后，**输入数字1来安装**。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/hy2.png)

没有域名就选择数字3

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy001.png)

自签证书可以输入bing.com

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy002.png)

选择数字1，正确

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy003.png)

选择数字1，udp类型

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy004-2.png)

端口可以回车随机

关于是否启用端口跳跃/多端口模式，一般选择2，跳过。如果封锁严重的时候可以选择1，启用。如果启用端口跳跃/多端口模式，需要按照提示输入开始端口和结束端口。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy005.png)

延迟、上传速度、下载速度、密码都可以用默认的配置，也可以自己修改，默认就回车

关于验证方式，一般选择1，auth_str(默认)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy006.png)

关于客户端名称，默认就回车

接下来会等待几分钟，成功后会出现“安装完成，请查看下方配置详细信息”。如果失败会有相应的提示，一般解决方法就是卸载脚本后重新安装。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy007.png)


带大括号的就是整个配置信息，需要复制下来，用鼠标右键有复制。在电脑上新建一个**config.json**的文件，把配置信息粘帖进去。需要**注意**的是：**有两行必须删除**，不然会无法启动hysteria客户端。这两行信息是：

"acl": "acl/routes.acl",

"mmdb": "acl/Country.mmdb",

**连带标点符号一起删除。**

有了配置文件，接下来就是下载hysteria客户端。

***

【hysteria 1客户端下载及使用方法】

hysteria 1官方客户端下载地址：https://github.com/apernet/hysteria/releases/tag/v1.3.5

根据电脑系统进行下载，电脑windows 32位系统就下载[hysteria-windows-386.exe](https://github.com/HyNetwork/hysteria/releases/download/v1.3.5/hysteria-windows-386.exe) 64位系统可以用[hysteria-windows-386.exe](https://github.com/HyNetwork/hysteria/releases/download/v1.3.5/hysteria-windows-386.exe)  或者[hysteria-windows-amd64.exe](https://github.com/HyNetwork/hysteria/releases/download/v1.3.5/hysteria-windows-amd64.exe)

hysteria客户端下载好后，将config.json配置文件放在同一级目录就能启动了。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/hy8.png)

启动hysteria，浏览器代理设置成和配置文件一样就行，配置文件包含http和socks5代理，http代理默认的是127.0.0.1和10809，socks5代理默认的是127.0.0.1和10808，端口号可以修改，浏览器二选一，端口号和配置文件一致。

如果按照默认来设置浏览器，可以设置成http127.0.0.1和10809 或者socks5 127.0.0.1和10808

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/vultr/hy10.png)

启动客户端后，出现connected和running字样表示启动成功。如果没有启动成功，请检查配置信息是否设置正确以及与服务器一致。

谷歌浏览器chrome可配合switchyomega插件来使用，下载插件：[switchyomega](https://github.com/atrandys/trojan/releases/download/1.0.0/SwitchyOmega_Chromium.crx)

安装插件，打开chrome，打开扩展程序，将下载的插件拖动到扩展程序页面，添加到扩展。
![20181116000534](https://user-images.githubusercontent.com/12132898/70548725-0461d000-1bae-11ea-9d1e-4577e36ac46e.png)

完成添加，会跳转到switchyomega页面，点跳过教程，然后点击proxy，如图填写，最后点击应用选项。
![20181116001438](https://user-images.githubusercontent.com/12132898/70548727-04fa6680-1bae-11ea-99da-568af4fd6f5f.png)

（注意：如果按照默认配置来设置，图片中的1080端口需要改为10808）

***

**常见问题及解决方法**：

**1、搭建的账号之前能用，突然不能用了，怎么解决？**

A：如果ip不能ping通，xshell不能直接连接vps服务器，说明ip被墙了，需要换ip。vultr开通和删除服务器非常方便，新服务器即新ip，为了保证开通的新服务器ip和旧ip不一样，先开新服务器出现ip后再删旧服务器。其它大多数vps服务商换ip都要额为收费。

B: 如果ip正常，那么多半是端口号被封了，此时需要换端口号，可以重新搭建。

2、需要安装bbr加速吗？

bbr加速是tcp加速，而hysteria是Quic(udp)协议。所以不用再部署bbr加速，当然自己想部署也可以，部署bbr加速可参考其它教程。

3、如何安装hysteria 2？

Hysteria 2 继承了 Hysteria 1.x 的几乎所有功能，同时引入了各种新的修复和增强。但值得注意的是，由于协议和代码经过了重大更改，Hysteria 2 与 Hysteria 1.x 完全不兼容。 用户必须在客户端和服务器上使用一致的版本。安装Hysteria 2后客户端请使用2.0及以上版本。

***

**hysteria 2一键部署管理脚本：**

```bash
wget -N --no-check-certificate https://raw.githubusercontent.com/flame1ce/hysteria2-install/main/hysteria2-install-main/hy2/hysteria.sh && bash hysteria.sh
```

***

> 如果输入安装命令后提示wget: command not found，那是因为服务器系统没有自带wget命令，安装一下wget。

> CentOS系统安装curl命令：yum install -y wget

> Debian/Ubuntu系统安装curl命令：apt-get install -y wget

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy2-001.jpg)

输入安装脚本后，选择数字1安装程序。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy2-002.jpg)

协议证书申请方式选择1。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy2-003.jpg)

端口可以自己填写想要的，也可以回车随机。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy2-004.jpg)

端口模式一般选择1，单端口模式。如果封锁严重的时候可以选择2，启用端口跳跃/多端口模式。如果启用端口跳跃，需要按照提示输入开始端口和结束端口。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy2-005.jpg)

端口可以自己填写想要的，也可以回车随机。

伪装网站地址回车。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy2-006.jpg)

最后出现这一步就成功了。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy2-007.jpg)

这一部分就是客户端配置信息，可以复制下来。新建名字为config.json文件，将客户端配置信息复制进去并保存。

hysteria 2的v2.2.3版本下载：https://github.com/apernet/hysteria/releases/download/app%2Fv2.2.3/hysteria-windows-386.exe

hysteria 2更新地址：https://github.com/apernet/hysteria/releases

将下载后的hysteria-windows-386.exe文件和config.json文件放在同一目录，双击运行ysteria-windows-386.exe就可以启动了。需要注意的是，脚本搭建后默认的代理端口是5678，那么浏览器代理端口也要填写socks5 127.0.0.1 5678 , 当然你也可以在客户端配置信息文件修改5678端口。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/hy2-008.jpg)

***


有问题可以发邮件至海外邮箱rebeccalane27@gmail.com
