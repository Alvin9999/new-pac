**2025年7月11日更新。**

***

**介绍**:

ProxySU是一款windows科学上网搭建软件，**不用输入代码、不用脚本**，支持一键搭建V2ray，Xray，Trojan，NaiveProxy, Trojan-Go, Hysteria, Brook, MTProto Go, ShadowsocksR(SSR),Shadowsocks-libev及相关插件一键安装工具。

**使用提醒**：

ProxySU的安装流程，是假设在全新系统下，没有装过以上代理软件，如果已经安装过，最好将系统重装一下，会减少很多的麻烦。ProxySU在开发过程中，一般都是在[vultr](https://www.vultr.com/?ref=7048874)的vps中测试，测试系统版本为：Centos7/8 Debian9/10 Ubuntu18.04/20.04(推荐Debian10)。[ProxySU官网](https://github.com/proxysu/ProxySU)。


ProxySU-v2.2.2示意图:

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps1.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps11.jpg)

**搭建流程**:

第一步:购买服务器获得ip和密码

第二步:ProxySU下载及搭建


***

**第一步:购买服务器获得ip和密码**

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

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/debian110908.png)

点击图中的系统名字，会弹出具体系统版本，推荐Debian系统，不推荐用CentOS系统，CentOS系统用ProxySU无法自动开启bbr加速。

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

**第二步:ProxySU下载及搭建**

当前提供下载的版本为ProxySU-v2.5.7,文件很小,大小为798kb. ProxySU-v2.5.7是比较老的版本，保留了SSR和SS搭建，最新版不支持。除了SSR、SS，还可以搭建v2ray、trojan等，如果搭建的协议有TLS字样就需要域名，如果没有TLS就不用域名。

ProxySU-v2.5.7：

[国外云盘下载1](https://download.574981.xyz/ProxySU-v2.5.7.zip)  [国外云盘下载2](https://d.dtku35.xyz/ProxySU-v2.5.7.zip)  

[ProxySU最新版](https://github.com/proxysu/ProxySU/releases)

## Windows系统需要安装net4.0及以上

[Microsoft.NET Framework 4.0](https://dotnet.microsoft.com/download/dotnet-framework/thank-you/net40-offline-installer) or higher

打开ProxySU,填上第一步购买的vps服务器ip和密码后,选上想搭建的科学上网工具。步骤如下：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps1.jpg)

**填上ip和密码，端口22和root默认。注意：ProxySU-v2.5.7版本，就算没有域名，在界面上也需要填写1个邮箱，可以是真实的，也可以随便填写1个，比如[123456@gmail.com](mailto:123456@gmail.com) 不然软件无法正常运行。**

***

**演示1:以搭建SSR为例，选中SSR模板库。**

注意：服务器系统推荐Debian11或者Ubuntu 20.04，SSR脚本不支持版本较高的系统，会导致SSR无法启动成功。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ssr0908-1.png)

SSR模板库只有SSR+TLS+Caddy，需要域名，第一次购买域名，可以参考这个[域名购买教程](https://github.com/Alvin9999/new-pac/wiki/%E5%9F%9F%E5%90%8D%E8%B4%AD%E4%B9%B0%E6%95%99%E7%A8%8B) 。证书申请需要填写一个邮箱，可以填写真实的，也可以随便填写一个，比如123455@gmail.com

伪装域名可以不填，如果填写，可以填写一个在大陆可以访问的域名，比如bing.com、www.microsoft.com等，伪装域名前面不要加https://

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ssr0908-3.png)

出现上面这个信息显示就是搭建成功了。Debian系统搭建过程中会开启bbr加速。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ssr0908-6.png)

搭建完成后会弹出账号信息，可以手动填写到SSR客户端，也可以复制一键导入链接。


***

**演示2：以搭建v2ray为例，选中v2ray模板库。**

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ssr0908-4.png)

注意：ProxySU-v2.5.7版本，就算没有域名，在界面上也需要填写1个邮箱，可以是真实的，也可以随便填写1个，比如123456@gmail.com  不然软件无法正常运行。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v2ray0910-1.png)

**在v2ray模板库中，选中想要搭建的v2ray协议，有的协议不需要域名，可以直接搭建，有的需要域名，所以需要提前购买域名并绑定服务器ip。如果搭建的协议有TLS字样就需要域名，如果没有TLS就不用域名。第一次购买域名，可以参考这个[域名购买教程](https://github.com/Alvin9999/new-pac/wiki/%E5%9F%9F%E5%90%8D%E8%B4%AD%E4%B9%B0%E6%95%99%E7%A8%8B) 。**

websocket+tls+web协议：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v2ray0910-2.png)

websocket协议：

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v2ray0910-3.png)

点击确定

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v2ray0910-4.png)

点击v2ray一键安装，软件会自动搭建

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/v2ray0910-5.png)

如果服务器是Debian或Ubuntu系统，软件会自动开启bbr加速

部署完后，会自动弹出帐号配置信息，并且在文件夹中也会自动生成相关配置文件及客户端下载地址

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps7.jpg)

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps8.jpg)

有个vmess地址，把它复制下来，然后右键“v2rayN”图标，选择“从剪切板批量导入url”，如下图

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/111.jpg)

如果忘记了vmes地址，在文件夹中有url的txt文档

***

**演示3：以搭建trojan为例，选中trojan模板库。**

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/trojan0908-1.png)

填写服务器ip、服务器密码、端口22、用户root、email

绑定服务器ip的域名、伪装网站(选填)

最后点击trojan一键安装

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/trojan0908-2.png)

出现上面这个信息显示就是搭建成功了。Debian系统搭建过程中会开启bbr加速。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/trojan0908-3.png)

最后会弹出账号信息。

***

**除了这个工具，还可以使用SSH工具连接vps后使用一键脚本来搭建。参考以下教程**：

| 教程名称 | 教程名称 |
|----------|----------|
| [自建 Shadowsocks/SSR 服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAss%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) | [自建 Hysteria 服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAhysteria%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) |
| [自建 V2Ray 服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAv2ray%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) | [自建 Trojan 服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAtrojan%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) |
| [一键搭建多个协议节点教程](https://github.com/Alvin9999/new-pac/wiki/%E4%B8%80%E9%94%AE%E6%90%AD%E5%BB%BA%E5%A4%9A%E4%B8%AA%E5%8D%8F%E8%AE%AE%E8%8A%82%E7%82%B9%E6%95%99%E7%A8%8B) | [一键搭建科学上网工具 ProxySU 教程](https://github.com/Alvin9999/new-pac/wiki/%E4%B8%80%E9%94%AE%E6%90%AD%E5%BB%BA%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91%E5%B7%A5%E5%85%B7ProxySU) |
| [VPS 解锁 ChatGPT、Netflix 等教程](https://github.com/Alvin9999/new-pac/wiki/vps%E8%A7%A3%E9%94%81ChatGPT%E3%80%81Netflix%E7%AD%89%E7%BD%91%E7%AB%99%E6%95%99%E7%A8%8B) | |

***

有问题可以发邮件至海外邮箱rebeccalane27@gmail.com
