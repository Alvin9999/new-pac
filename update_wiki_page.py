import re
import os
from datetime import datetime
import pytz  # 引入时区库

# ====== 文件路径设置 ======
wiki_file = os.path.join("wiki", "直翻通道.md")  # Wiki 仓库中的文件
readme_file = os.path.join("README.md")  # 主仓库根目录下的 README.md 文件

# ====== 获取当前北京时间 ======
shanghai_tz = pytz.timezone("Asia/Shanghai")
current_time = datetime.now(shanghai_tz).strftime("%Y年%m月%d日%H点%M分")

# ====== 更新 Wiki 页面 ======
if not os.path.exists(wiki_file):
    raise FileNotFoundError(f"{wiki_file} 不存在，请检查路径。")

with open(wiki_file, "r", encoding="utf-8") as file:
    content = file.read()

# 定义更新域名的函数（递增域名中的数字部分）
def increment_domain(match):
    base = match.group(1)
    num = int(match.group(2)) + 1  # 数字加 1
    suffix = match.group(3)
    return f"{base}{num}{suffix}"

# 更新域名数字，适配单个域名 379800.xyz
updated_content = re.sub(r"(fan)(\d+)(\.379800\.xyz)", increment_domain, content)

# 替换时间部分为当前北京时间
updated_content = re.sub(
    r"北京时间\d{4}年\d{2}月\d{2}日\d{2}点\d{2}分更新",
    f"北京时间{current_time}更新",
    updated_content
)

# 写回更新内容
with open(wiki_file, "w", encoding="utf-8") as file:
    file.write(updated_content)

print(f"Wiki 页面内容已更新：当前北京时间为 {current_time}")

# ====== 更新 README.md 文件 ======
if not os.path.exists(readme_file):
    raise FileNotFoundError(f"{readme_file} 不存在，请检查路径。")

with open(readme_file, "r", encoding="utf-8") as file:
    readme_content = file.read()

# 替换 README.md 中的更新时间
updated_readme_content = re.sub(
    r"北京时间\d{4}年\d{2}月\d{2}日\d{2}点\d{2}分更新",
    f"北京时间{current_time}更新",
    readme_content
)

# 写回更新内容
with open(readme_file, "w", encoding="utf-8") as file:
    file.write(updated_readme_content)

print(f"README.md 内容已更新：当前北京时间为 {current_time}")
