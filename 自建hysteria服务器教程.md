一键安装sing-box脚本，开箱即用 18 个节点（直连 9 + WARP 9），包括4个 hysteria2 节点，含端口一键切换、BBR 加速、分享链接导出等。支持 Debian/Ubuntu/CentOS/Arch Linux/Fedora/Rocky/openSUSE Linux 系统，已在[Vultr](https://www.vultr.com/?ref=7048874) 上测试通过。脚本地址：[Alvin9999/Sing-Box-Plus](https://github.com/Alvin9999/Sing-Box-Plus)

```bash
wget -O sing-box-plus.sh https://raw.githubusercontent.com/Alvin9999/Sing-Box-Plus/main/sing-box-plus.sh && chmod +x sing-box-plus.sh && bash sing-box-plus.sh
```
> 安装完成后，输入 bash sing-box-plus.sh 可进入管理页面。

> 如果安装过其它 sing-box 脚本，请先卸载。

***

**脚本演示**

复制上面安装命令代码到VPS服务器里，复制代码用鼠标右键的复制，然后在vps里面右键粘贴进去，因为ctrl+c和ctrl+v无效。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-sing-box-1.png)

复制脚本后，按回车键。

![](https://cdn.jsdelivr.net/gh/Alvin9999/pac2/softimag/2025-sing-box-2.png)

输入数字 1 安装脚本。脚本全自动安装。

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

脚本还有其它功能：查看分享链接、一键更换所有端口 、一键开启 BBR。


***


有问题可以发邮件至海外邮箱rebeccalane27@gmail.com
