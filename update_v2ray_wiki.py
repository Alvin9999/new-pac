import re
import os
from datetime import datetime
import pytz
import base64
import json

# ====== 文件路径设置 ======
wiki_file = os.path.join(os.path.dirname(__file__), "v2ray_free_account.md")  # Wiki 文件的路径

# ====== 获取当前北京时间 ======
shanghai_tz = pytz.timezone("Asia/Shanghai")
current_time = datetime.now(shanghai_tz).strftime("%Y年%m月%d日%H点%M分")

# ====== 读取文件内容 ======
if not os.path.exists(wiki_file):
    raise FileNotFoundError(f"{wiki_file} 文件不存在，请检查路径。")

with open(wiki_file, "r", encoding="utf-8") as file:
    content = file.read()

# ====== 提取当前的 host ======
host_match = re.search(r"(y)(\d+)(\.582185\.xyz)", content)
if not host_match:
    raise ValueError("未找到有效的 host 格式，请检查文件内容。")

current_host_num = int(host_match.group(2))  # 提取当前 host 的数字部分
next_host_num = current_host_num + 1         # 计算下一次的数字

# ====== 更新伪装域名（host） ======
def increment_host(match):
    base = match.group(1)  # "y"
    suffix = match.group(3)  # ".582185.xyz"
    return f"{base}{next_host_num}{suffix}"  # 替换为下一个数字

# 更新 host
updated_content = re.sub(r"(host\):\s+y)(\d+)(\.582185\.xyz)", increment_host, content)

# ====== 更新节点一键导入链接中的 host ======
updated_content = re.sub(r"(\"host\":\s+\"y)(\d+)(\.582185\.xyz\")", increment_host, updated_content)

# ====== 更新 vmess 链接 ======
def update_vmess(match):
    # 解码 Base64
    vmess_json = json.loads(base64.b64decode(match.group(1)).decode('utf-8'))
    # 更新 host
    if "host" in vmess_json:
        base, num, suffix = re.match(r"(y)(\d+)(\.582185\.xyz)", vmess_json["host"]).groups()
        vmess_json["host"] = f"{base}{next_host_num}{suffix}"
    # 更新 Base64 编码后的 vmess 链接
    return f"vmess://{base64.b64encode(json.dumps(vmess_json).encode('utf-8')).decode('utf-8')}"

updated_content = re.sub(r"vmess://([A-Za-z0-9+/=]+)", update_vmess, updated_content)

# ====== 更新更新时间 ======
updated_content = re.sub(
    r"更新时间：\s+北京时间\d{4}年\d{2}月\d{2}日\d{2}点\d{2}分",
    f"更新时间： 北京时间{current_time}",
    updated_content,
)

# ====== 写回更新内容 ======
with open(wiki_file, "w", encoding="utf-8") as file:
    file.write(updated_content)

print(f"更新完成：节点 Host 已更新为 y{next_host_num}.582185.xyz，当前北京时间为 {current_time}。")
