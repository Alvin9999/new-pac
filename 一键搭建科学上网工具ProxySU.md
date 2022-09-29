**2022年9月15日更新。**

**2022年4月12日更新ProxySU的推荐版本v2.4.0，解决提示域名解析错误的问题。注意：ProxySU官网的最新版已经去掉了很多款工具的搭建模块，如果想按照教程那样搭建SSR等工具，可以下载旧版，本页面也有下载ProxySU-v2.4.0旧版的地址。**

***


**介绍**:

ProxySU是一款windows科学上网搭建软件，**不用输入代码、不用脚本**，支持一键搭建V2ray，Trojan，NaiveProxy, Trojan-Go, ShadowsocksR(SSR),Shadowsocks-libev及相关插件一键安装工具。

**使用提醒**：

ProxySU的安装流程，是假设在全新系统下，没有装过以上代理软件，如果已经安装过，最好将系统重装一下，会减少很多的麻烦。ProxySU在开发过程中，一般都是在[vultr](https://www.vultr.com/?ref=7048874)的vps中测试，测试系统版本为：Centos7/8 Debian9/10 Ubuntu18.04/20.04(推荐Debian10)。[ProxySU官网](https://github.com/proxysu/windows/tree/v2.2.2)。

**ProxySU-v2.2.2功能如下:**

##### V2ray可一键安装的模式有：
* tcp 
* tcp+http伪装  
* tcp+TLS 
* tcp+TLS （自签证书）
* Vless+tcp+TLS+Web (新热门协议)
* WebSocket
* WebSocket+TLS 
* WebSocket+TLS+Web 
* WebSocket+TLS（自签证书） 
* http2  
* http2+TLS+Web
* http2（自签证书）
* mKCP及各种伪装 
* QUIC及各种伪装。  
注：mKCP和QUIC模式使用udp协议，可以有效减少网络延时，有加速的作用，但在网络管控严厉时期，会导致IP被封，遇到的一次，就是刚安装好，使用了3个小时后，IP被封（现已确认是mKCP的流量被识别导致，项目组正在维护中。2020.6.10维护完毕，升级到版本4.24.2及以上，启用mKCP密钥可增强抗识别）。以上模式最推荐的是WebSocket+TLS+Web 和http2+TLS+Web 需要有一个域名。如果能加上CDN则稳定性更好。加上CDN后，是加速还是减速，与线路有关。

##### Trojan 可一键安装：  
* Trojan + TLS + Web

##### Trojan-Go 可一键安装：  
* Trojan-Go + TLS + Web  
* Trojan-Go + WebSocket + TLS + Web

##### NaiveProxy一键安装：  
* NaiveProxy + TLS +Web  

##### ShadowsocksR(SSR)一键安装：  
* SSR+TLS+Caddy  

##### Shadowsocks-libev及相关插件一键安装：  
* SS 经典模式  
* SS+WebSocket+TLS+Caddy(Web前置) (推荐)  
* SS+WebSocket  
* SS+QUIC  
* SS+kcptun  
* SS+obfs+http+Web  
* SS+obfs+TLS+Web  

##### 支持的VPS系统为：  
* CentOS 7/8   
* Debian 8/9/10 (推荐Debian10)  
* Ubuntu 16.04及以上

示意图:

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps1.jpg)

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps11.jpg)

**搭建流程**:

第一步:购买服务器获得ip和密码

第二步:ProxySU下载及搭建


***

**第一步:购买服务器获得ip和密码**

VPS服务器需要选择国外的，首选国际知名的vultr，速度不错、稳定且性价比高，按小时计费，能够随时开通和删除服务器，新服务器即是新ip。

vultr注册地址：https://www.vultr.com/?ref=7048874 （vps最低2.5美元/月，vultr全球25个服务器位置可选，包括洛杉矶、韩国、新加坡、日本、德国、荷兰等。支持支付宝和paypal付款。） 

<a href="https://www.vultr.com/?ref=7048874 "><img src="https://www.vultr.com/media/banners/banner_728x90.png" width="728" height="90"></a>

虽然是英文界面，但是现在的浏览器都有网页翻译功能，鼠标点击右键，选择网页翻译即可翻译成中文。

注册并邮件激活账号，充值后即可购买服务器。充值方式是支付宝或paypal，使用paypal有银行卡（包括信用卡）即可。paypal注册地址：https://www.paypal.com （paypal是国际知名的第三方支付服务商，注册一下账号，绑定银行卡即可购买国外商品）

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

电信用户推荐洛杉矶服务器；联通、移动用户推荐韩国、洛杉矶服务器。其它位置也可以尝试。

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new4.PNG)

**点击图中的系统名字，会弹出具体系统版本，推荐Debain10。不推荐用CentOS7，CentOS7用ProxySU无法自动开启bbr加速。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new5.PNG)

选择服务器套餐。根据自己的需求来选择，如果服务器位置定了，套餐不影响速度，影响流量和配置，一般用的人数少，选择低配置就够了。

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new6.PNG)

关闭自动备份，这个是收费的，可以关闭它。

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/new7.PNG)

最后点击“Deploy Now”开始部署，等2~3分钟就差不多了。此时也会收到vultr官方发来的“Cloud Server Activated”邮件提醒。

**完成购买后，找到系统的密码记下来，部署服务器时需要用到。vps系统的密码获取方法如下图：**

![](https://fastly.jsdelivr.net/gh/Alvin9999/crp_up/pac教程05.png)

![](https://fastly.jsdelivr.net/gh/Alvin9999/crp_up/pac教程06.png)

**删掉服务器步骤如下图**：

删除服务器时，先开新的服务器后再删除旧服务器，这样可以保证新服务器的ip与旧ip不同。

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/ss/de4.PNG)

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/ss/de2.PNG)

![](https://fastly.jsdelivr.net/gh/Alvin9999/PAC/ss/de5.png)

**第二步:ProxySU下载及搭建**

当前提供下载的版本为ProxySU-v2.4.0,文件很小,大小为569kb.注意：ProxySU官网的最新版已经去掉了很多款工具的搭建模块，如果想按照教程那样搭建SSR等工具，可以下载旧版。

[国外云盘下载1](https://d2.freessr2.xyz/ProxySU-v2.4.0.zip)  [国外云盘下载2](https://d1.freessr1.xyz/ProxySU-v2.4.0.zip)  


**如果在安装过程中总是提示某个错误，也可以尝试其它ProxySU版本，官方其它版本下载**：https://github.com/proxysu/ProxySU/releases

## Windows系统需要安装net4.0及以上

[Microsoft.NET Framework 4.0](https://dotnet.microsoft.com/download/dotnet-framework/thank-you/net40-offline-installer) or higher

打开ProxySU,填上第一步购买的vps服务器ip和密码后,选上想搭建的科学上网工具。步骤如下：

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps1.jpg)

**填上ip和密码，端口22和root默认。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps10.jpg)

**以搭建v2ray为例，选中v2ray模板库。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps3.jpg)

**在v2ray模板库中，选中想要搭建的v2ray协议，有的协议不需要域名，可以直接搭建，有的需要域名，所以需要提前购买域名并绑定服务器ip。第一次购买域名，可以参考这个[域名购买教程](https://github.com/Alvin9999/new-pac/wiki/%E5%9F%9F%E5%90%8D%E8%B4%AD%E4%B9%B0%E6%95%99%E7%A8%8B) 。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps4.jpg)

**目前比较热门的v2ray协议:WebSocket+Tls+Web （需要域名）选中后，填写域名。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps5.jpg)

**如果没有域名，可以搭建其它的协议，比如TCP、WebSocket（不带tls）、KCP。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps9.jpg)

**点击v2ray一键安装，软件会自动搭建。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps6.jpg)

**系统工具：点击系统工具可以校对时间和部署bbr加速。v2ray需要校对时间。目前搭建v2ray的过程中，软件会自动校对时间和开启bbr加速，如果一切顺利不用手动再去点击系统工具。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps11.jpg)

**部署完后，会自动弹出帐号配置信息，并且在文件夹中也会自动生成相关配置文件及客户端下载地址。**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps7.jpg)

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/ps8.jpg)

**有个vmess地址，把它复制下来，然后右键“v2rayN”图标，选择“从剪切板批量导入url”，如下图**

![](https://fastly.jsdelivr.net/gh/Alvin9999/pac2/softimag/111.jpg)

**如果忘记了vmes地址，在文件夹中有url的txt文档。**

***

**除了这个工具，还可以使用SSH工具连接vps后使用一键脚本来搭建。参考以下教程**：

[自建ss/ssr服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAss%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 
[自建v2ray服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAv2ray%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 
[自建hysteria服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAhysteria%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 
[自建brook服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAbrook%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 
[自建trojan服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAtrojan%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 
[自建WireGuard VPN服务器教程](https://github.com/Alvin9999/new-pac/wiki/%E8%87%AA%E5%BB%BAWireGuard-VPN%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%95%99%E7%A8%8B) 

***

有问题可以发邮件至海外邮箱kebi2014@gmail.com
