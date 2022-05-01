**2022年3月17日更新开通服务器教程。**

**如果无法查看图片，可以访问https://tr1.freeair888.club/自建wireguard服务器教程/**

***


**wireguard简介**： Wireguard是一种新型的VPN协议，相比目前主流的VPN协议，WireGuard具有轻便、快速、高效、安全的优点，被称为下一代VPN协议。WireGuard最初是为Linux内核开发，但目前已提供跨平台支持，可在Linux、安卓、苹果iOS、MacOS、Openwrt、Windows等多个平台使用 。

wireguard可以全局代理电脑所有软件，包括浏览器、游戏软件等。

**注意**：WireGuard 是通过 UDP 协议传输数据的，这意味着它可以搭建在被墙的服务器上使用，复活被墙IP！

**同时**：因为是 UDP 传输的，所以也不怕被墙，锐速、BBR 这类TCP加速工具也不会对其起到加速作用。

**另外**：如果你当地运营商对海外 UDP 链接进行 QOS 限速，那么速度可能不如使用 TCP 链接的代理软件理想。

***

**整个教程分三步**：

第一步：购买VPS服务器

第二步：一键搭建服务器

第三步：客户端TunSafe配置账号

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

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/pp100.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/pp101.png)


**vultr改版了，最新开通服务器步骤如图**：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new1.PNG)

选择“Cloud Compute”。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new2.PNG)

选择“Regular Performance”。如果选择这个，在下面选择具体套餐的时候，最低是3.5美元/月（也要看服务器位置），流量是500GB/月；5美元是1T流量/月。

如果选择前面3个，在下面选择具体套餐的时候，最低是5美元/月，但5美元是2T流量/月。也就是，对流量需求较高的可以选择前面3个。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new3.PNG)

选择服务器位置。不同的服务器位置速度会有所不同，有的服务器的最低价格会不同，一般纽约等位置的价格最低，有3.5美元/月的，可根据自己的需求来选择。

可以优先尝试洛杉矶服务器，亚洲服务器日本、韩国延迟较低，但用的人很多，国内速度不一定就会很好，当然其它服务器位置也可以尝试。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new4.PNG)

**点击图中的系统名字，会弹出具体系统版本， 搭建脚本只支持CentOS7或CentOS8 **

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new5.PNG)

选择服务器套餐。根据自己的需求来选择，如果服务器位置定了，套餐不影响速度，影响流量和配置，一般用的人数少，选择低配置就够了。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new6.PNG)

关闭自动备份，这个是收费的，可以关闭它。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/new7.PNG)

最后点击“Deploy Now”开始部署，等3~5分钟就差不多了。

**开通服务器时，当出现了ip，不要立马去ping或者用xshell去连接，再等3~5分钟之后，有个缓冲时间。完成购买后，找到系统的密码记下来，部署服务器时需要用到。vps系统（推荐centos6）的密码获取方法如下图：**

![](https://cdn.jsdelivr.net/gh/Alvin9999/crp_up/pac教程05.png)

![](https://cdn.jsdelivr.net/gh/Alvin9999/crp_up/pac教程06.png)

**删掉服务器步骤如下图**：

删除服务器时，先开新的服务器后再删除旧服务器，这样可以保证新服务器的ip与旧ip不同。

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/de4.PNG)

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/de2.PNG)

![](https://cdn.jsdelivr.net/gh/Alvin9999/PAC/ss/de5.png)


***

**第二步：部署VPS服务器**

购买服务器后，需要部署一下。因为你买的是虚拟东西，而且又远在国外，我们需要一个叫Xshell的软件来远程部署。Xshell windows版下载地址：

[国外云盘1下载](https://tr601.free4444.xyz/Xshell_setup_wm.exe)
[国外云盘2下载](https://tr201.free4444.xyz/Xshell_setup_wm.exe)

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

**一键安装wirguard脚本代码（Centos7/Centos8）**：

***

curl -O https://raw.githubusercontent.com/atrandys/wireguard/master/wg_mult.sh && chmod +x wg_mult.sh && ./wg_mult.sh

***

复制上面整个代码到vps服务器中 。复制后如果不动按回车键。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire1.jpg)

输入数字1进行安装，2是卸载。一键脚本会自动安装，一般几分钟就能安装好，很快。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire2.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire3.jpg)

安装到这个界面就结束了。上述是二维码界面，不用管。鼠标往上滑动会看到这个提示，需要把 /etc/wireguard/client.conf文件下载到电脑上。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire4.jpg)

有两种方法。一种是输入命令 cat /etc/wireguard/client.conf ，信息就会展示出来，如下来。然后复制（鼠标左键选中，右键选择复制），新建一个 client.conf 文件，把内容粘贴进去并保存即可。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire5.jpg)

第二种方法是直接把这个文件下载下来。 先安装下载文件的命令：

yum -y install lrzsz 

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire6.jpg)

安装结束后输入如下命令就可以把client.conf文件下载到电脑上。

sz /etc/wireguard/client.conf

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire7.PNG)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire8.jpg)

这样，wireguard的账号配置信息就搭建好了。 接着下载安装TunSafe，这是wireguard windows版第三方开发软件，也可以去wireguard.com官网，下载官方的Windows版客户端，推荐用tunsafe。

**增加wireguard多用户方法**：

1、进入下载脚本的路径，然后使用以下命令打开脚本

./wg_mult.sh

2、选择4 add user

3、然后输入一个用户名，不要和之前的重复

4、然后获取新用户名.conf文件即可

***

第三步：客户端TunSafe使用方法

PC端：

TunSafe 官网下载：https://tunsafe.com/download ，下载TunSafe-1.5-rc2.exe 文件大小：607k 国外网盘下载

下载后双击安装。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire13.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire10.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire11.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire12.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire14.jpg)

出现上述界面就安装好了，点击close关闭。

打开TunSafe，选择File—Import File，把 client.conf文件 导入进去

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire15.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire16.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire17.jpg)

导入client.conf文件后，点击Connect进行连接。出现如下标志就是连接成功啦。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire18.jpg)

这个软件是全局代理软件，也就是电脑上所有的软件都被代理了，所以建议上外网网就专门上网，国内软件最好关闭。下图是网友在白天测试的YouTube速度图，晚上高峰期会慢一些， 供参考。国内各个地区封锁不同，效果肯定也会不同。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/test2.jpg)

以上就是windows系统使用账号的方法。

TunSafe尚没有针对Linux，OSX或FreeBSD的图形用户界面。但是，您可以从源代码编译TunSafe，并在命令提示符下运行它，用户指南。

手机端：

手机端除了可以通过导入配置文件的方法配置，也可以PC端把配置信息生成二维码，然后手机端就可以通过二维码来扫描了，要方便点。

二维码生成网址： https://cli.im/

二维码生成方法：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire-erwei1.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire-erwei2.jpg)


安卓版：WireGuard.apk [国外云盘下载](https://f-droid.org/repo/com.wireguard.android_491.apk) [国外云盘2下载](https://tr601.free4444.xyz/com.wireguard.android_491.apk)

安卓版安卓wireguard后，选择右下角的+号按钮进行配置，可以选择第一个将配置文件导入进去，也可以选择第二个扫描二维码。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire-an2.jpg)

iOS用国外ID在国外商店搜索 tunsafe 或 wireguard 下载。[iOS注册美区Apple ID教程](https://github.com/Alvin9999/new-pac/wiki/iOS%E6%B3%A8%E5%86%8C%E7%BE%8E%E5%8C%BAApple-ID%E6%95%99%E7%A8%8B) 

iOS安装tunsafe后，打开配置设置。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire-ios1.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire-ios2.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire-ios3.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire-ios4.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/wire/wire-ios5.jpg)

同样可以选择第一个将文件导入进去，或者第二个扫描配置文件的二维码。



***


有问题可以发邮件至海外邮箱kebi2014@gmail.com
